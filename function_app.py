import azure.functions as func
import logging
import base64
import json

from openai_whisper import transcribe_audio_from_url
from db import MongoDB
from az_queue import Queue
import config

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="q-audios-to-transcribe",
                               connection="ftrgp01blobstore_STORAGE") 
def q_trigger_audios_to_transcribe(azqueue: func.QueueMessage):
  """
  - Pull base64 string from queue
  - Convert it into json
  - Extract blobUrl & DB records Id
  - Update DB with {status: "TRANSCRIBING"}
  - Get txion using blobUrl
  - Update DB with {status: "ANALYZING", transcription: <txion generated>}
  - Push Id to q-transcriptions-to-analyze
  - Exit from queue
  """
  try:
    # - Pull base64 string from queue
    base64_str = azqueue.get_body()
    
    # - Convert it into json
    json_str = base64.b64decode(base64_str).decode('utf-8')
    json_message = json.loads(json_str)
    logging.info(f'Queue trigger for {config.Q_AUDIOS_TO_TRANSCRIBE} dequeued a message: {json_message}')
    
    # - Extract blobUrl & DB records Id
    blob_url = json_message["blobUrl"]
    record_id = json_message["id"]
    
    # - Update DB with {status: "TRANSCRIBING"}
    mongo_client = MongoDB()
    mongo_client.update_one_by_id(id=record_id, upsert_data={"status": "TRANSCRIBING"})
    
    # - Get txion using blobUrl
    txion_generated = transcribe_audio_from_url(blob_url=blob_url)
    # txion_generated = "txion test" #! For Debugging
    
    # Update DB with {status: "ANALYZING", transcription: <txion_generated>}
    mongo_client.update_one_by_id(id=record_id, upsert_data={"status": "ANALYZING", "transcription": txion_generated})
    
    # - Push Id to q-transcriptions-to-analyze
    queue_client = Queue()
    queue_client.push({"id": record_id})
    
    # - Exit from queue
    print(f'Queue trigger for {config.Q_AUDIOS_TO_TRANSCRIBE} finished processing a message: {json_message}')
    
  except Exception as e:
    print(f"An error occurred while processing q-audios-to-transcribe: {e}")
    
