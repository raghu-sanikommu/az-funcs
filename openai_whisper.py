from openai import OpenAI
import time
import requests
import os
import tempfile

import config
from logger import logger


client = OpenAI(api_key=(config.OPENAI_API_KEY))
# Though audio in blob is .opus, we save it in .wav coz whisper doesn't support .opus
tempFilePath = tempfile.gettempdir()
fp = tempfile.NamedTemporaryFile(suffix=".wav")
print("Temp file name :: " + fp.name)
local_audio_path_wav = fp.name # For deployed server
# local_audio_path_wav = 'audio.wav' # For local server


def download_audio_file(blob_url, local_path = local_audio_path_wav):
  logger.info("Downloading audio file ...")
  response = requests.get(blob_url)
  response.raise_for_status() 
  with open(local_path, 'wb') as file:
    file.write(response.content)


def hit_whisper():
  audio_file = open(local_audio_path_wav, "rb")
  logger.info("Txion has started ...")
  start_time = time.time()
  transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    response_format="verbose_json",
    timestamp_granularities=["segment"]
  )
  end_time = time.time()
  logger.info(f"Time taken for txion: {end_time - start_time}")
  audio_file.close()
  transcription.txion_time = round(end_time - start_time, 2)
  return transcription


def delete_audio_file():
  logger.info("Cleaning up the directory ...")
  os.remove(local_audio_path_wav)
  logger.info("Cleaned the directory!")


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
    logger.info("Transcription is done")
    
    # - Clean up the downloaded file
    delete_audio_file()
    
    return txion
  except Exception as e:
    logger.info(f"An error occurred while transcribing: {e}")
