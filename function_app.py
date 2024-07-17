import azure.functions as func
import logging
import base64
import json

from openai_whisper import transcribe_audio_from_url

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="q-audios-to-transcribe",
                               connection="ftrgp01blobstore_STORAGE") 
def q_trigger_audios_to_transcribe(azqueue: func.QueueMessage):
    base64_str = azqueue.get_body()
    json_str = base64.b64decode(base64_str).decode('utf-8')
    json_message = json.loads(json_str)
    logging.info('Python Queue trigger processed a message: %s',
                json_message)
    transcribe_audio_from_url(blob_url=json_message["blobUrl"])
    
