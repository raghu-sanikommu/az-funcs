from openai import OpenAI
import time
import requests
import os


import config


client = OpenAI(api_key=(config.OPENAI_API_KEY))
local_audio_path_wav = "audios/audio.wav"


def download_audio_file(blob_url, local_path = local_audio_path_wav):
  print("Downloading audio file ...")
  response = requests.get(blob_url)
  response.raise_for_status() 
  with open(local_path, 'wb') as file:
    file.write(response.content)


def hit_whisper():
  audio_file = open(local_audio_path_wav, "rb")
  print("Txion has started ...")
  start_time = time.time()
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
  )
  end_time = time.time()
  print(f"Time taken for txion: {end_time - start_time}")
  audio_file.close()
  return transcription.text


def delete_audio_file():
  print("Cleaning up the directory ...")
  os.remove(local_audio_path_wav)


"""
- Download audio from blob (wav format)
- Pass it to OpenAI Whisper to get Txion
- Clean up the downloaded file
"""
def transcribe_audio_from_url(blob_url):
  try:
    # - Download audio from blob
    download_audio_file(blob_url)

    # - Pass it to OpenAI Whisper to get txion
    txion = hit_whisper()
    print(txion)
    
    # - Clean up the downloaded file
    delete_audio_file()
  except Exception as e:
    print(f"An error occurred while transcribing: {e}")
