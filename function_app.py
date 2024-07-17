import azure.functions as func
import logging

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="q-audios-to-transcribe",
                               connection="ftrgp01blobstore_STORAGE") 
def q_trigger_audios_to_transcribe(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
    print(azqueue.get_body().decode('utf-8'))
