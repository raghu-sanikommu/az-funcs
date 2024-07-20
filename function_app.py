import azure.functions as func
import base64
import json
import re
import time


from openai_whisper import transcribe_audio_from_url
from db import MongoDB
from az_queue import Queue
import config
import gemini_llm
import sample_txion
from logger import logger

app = func.FunctionApp()

@app.queue_trigger(arg_name="azqueue", queue_name="q-audios-to-transcribe",
                               connection="ftrgp01blobstore_STORAGE") 
def q_trigger_audios_to_transcribe(azqueue: func.QueueMessage):
  """
  - Pull base64 string from queue
  - Convert it into json
  - Extract blobUrl & DB records Id
  - Update DB with {status: "TRANSCRIBING"}
  - Pass audio to whisper and get verbose txion using blobUrl
  - Update DB with {status: "ANALYZING", transcription: <txion generated> ... and few more}
  - Push Id to q-transcriptions-to-analyze
  - Exit from queue
  """
  try:
    # - Pull base64 string from queue
    base64_str = azqueue.get_body()
    
    # - Convert it into json
    json_str = base64.b64decode(base64_str).decode('utf-8')
    json_message = json.loads(json_str)
    logger.info(f'Queue trigger for {config.Q_AUDIOS_TO_TRANSCRIBE} dequeued a message: {json_message}')
    
    # - Extract blobUrl & DB records Id
    blob_url = json_message["blobUrl"]
    record_id = json_message["id"]
    
    # - Update DB with {status: "TRANSCRIBING"}
    mongo_client = MongoDB()
    mongo_client.update_one_by_id(id=record_id, upsert_data={"status": "TRANSCRIBING"})
    
    # - Pass audio to whisper and get verbose txion using blobUrl
    txion_generated_verbose = transcribe_audio_from_url(blob_url=blob_url)
    # txion_generated_verbose = {"segments": [], "language": "lan", "duration": 0} #! For Debugging
    
    txion_generated = [{'id': segment['id'], 'start': segment['start'], 'end': segment['end'], 'text': segment['text'].strip()} for segment in txion_generated_verbose.segments]
    
    # Update DB with {status: "ANALYZING", transcription: <txion_generated> ... and few more}
    mongo_client.update_one_by_id(id=record_id, upsert_data={
      "status": "ANALYZING", 
      "transcription": txion_generated, 
      "txionTime": txion_generated_verbose.txion_time,
      "callDuration": txion_generated_verbose.duration,
      "language": txion_generated_verbose.language
    })
    
    # - Push Id to q-transcriptions-to-analyze
    queue_client = Queue()
    queue_client.push({"id": record_id})
    
    # - Exit from queue
    logger.info(f'Queue trigger for {config.Q_AUDIOS_TO_TRANSCRIBE} finished processing a message: {json_message}')
    
  except Exception as e:
    logger.info(f"An error occurred while processing q-audios-to-transcribe: {e}")
    


@app.queue_trigger(arg_name="azqueue", queue_name="q-transcriptions-to-analyze", connection="ftrgp01blobstore_STORAGE") 
def q_trigger_transcriptions_to_analyze(azqueue: func.QueueMessage):
  """
  - Pull base64 string from queue
  - Convert it into json
  - Extract DB records Id
  - Query MongoDB to get the txion of that record
  - Format txion to pass it for LLM
  - Pass txion to LLM and identify speakers & additional params
  - Update DB with {status: "COMPLETED", transcription: <txion_speaker_identified>}
  - Exit from queue
  """
  try:
    # - Pull base64 string from queue
    base64_str = azqueue.get_body()
    
    # - Convert it into json
    json_str = base64.b64decode(base64_str).decode('utf-8')
    json_message = json.loads(json_str)
    logger.info(f'Queue trigger for {config.Q_TRANSCRIPTIONS_TO_ANALYZE} dequeued a message: {json_message}')
    
    # - Extract DB records Id
    record_id = json_message["id"]
    
    # - Query MongoDB to get the txion of that record
    mongo_client = MongoDB()
    db_result = mongo_client.find_by_id(id=record_id)
    txion = db_result["transcription"]
    # txion = sample_txion.sample_txion #! For Debugging
    logger.info("Fetched txion from DB ...")
    
    # - Format txion to pass it for LLM
    sentences_to_llm = [{"id": segment["id"], "text": segment['text']} for segment in txion]
    
    # - Pass txion to LLM and identify speakers & additional params
    llm_prompt = f"""
    You are a powerful analyzing tool that can analyze conversation between a customer care agent and customer.


    {sentences_to_llm}


    From above array of objects containing "sentence" and "id" parameters where:
    - "sentence" defines the sentence spoke by either a customer care agent or a customer
    - "id" defines the index of object in the array
    Analyze the following parameters:

      1. Identify by whom each sentence is spoke by, and push the role along with its "id" separated by _ (underscore) into an array according to below criteria and put it in the json under the key 'segments':
        a. "id" is the index of "sentence" in the array
        b. If its agent, push '<id>_AGNT'
        c. If its customer, push '<id>_CUST'
        d. If you can't identify, push '<id>_NA'
        e. Make sure, you push the role for every sentence in the given array of sentences
      2. Identify overall sentiment in the conversation whether its 'positive' or 'negative' and push it into the json under the key 'overall_sentiment'
      3. Identify the crisp and short version of issue description and push it into the json under the key 'issue_description'
      4. Identify the crisp and short version of resolution provided and push it into the json under the key 'resolution_provided'
      3. Output only the json and nothing else

      Example:
      Input: ['Hello, welcome to Airtel Care, How may I help you?', 'Hi, I am unable to connect to my internet', 'Sorry for the inconvenience, let me look into it, please wait', 'Thanks for waiting, it seems your recharge has finished, please recharge to continue using internet', 'Thank You, will do that', 'You too, have a nice day']
      Output: {{ 'segments': ['0_AGNT', '1_CUST', '2_AGNT', '3_AGNT', '4_CUST', '5_AGNT'], 'overall_senitiment': 'positive', 'issue_description': 'Unable to connect to internet', 'resolution_provided': 'Recharge to continue using internet' }}
    """
    
    logger.info("Hitting LLM ...")
    start_time = time.time()
    analytics_from_llm = gemini_llm.gemini_model.generate_content(llm_prompt).text
    res = re.search(r'```json(.*?)```', analytics_from_llm, re.DOTALL)
    analytics_from_llm = res.group(1).strip()
    analytics_from_llm = json.loads(analytics_from_llm)
    logger.info("LLM processing is finished.")
    end_time = time.time()
    llm_time = round(end_time - start_time, 2)
    
    time_analytics = {
      "AGNT": 0,
      "CUST": 0,
      "NA": 0
    }
    for x in analytics_from_llm['segments']:
      [index, role] = x.split('_')
      txion[int(index)]['role'] = role
      user_time = txion[int(index)]['end'] - txion[int(index)]['start']
      time_analytics[role] += user_time
      

    upsert_data = {
      "status": "COMPLETED",
      "transcription": txion,
      "llmTime": llm_time,
      "txionAnalytics": {
        "overallSentiment": analytics_from_llm['overall_sentiment'],
        "issueDescription": analytics_from_llm['issue_description'],
        "resolutionProvided": analytics_from_llm['resolution_provided']
      },
      "timeAnalytics": {
        "agentTime": round(time_analytics["AGNT"], 2),
        "custTime": round(time_analytics["CUST"], 2),
        "unknownTime": round(time_analytics["NA"], 2)
      },
    }
    
    # - Update DB with {status: "COMPLETED", transcription: <txion_speaker_identified> ... and few others}
    mongo_client.update_one_by_id(id=record_id, upsert_data=upsert_data)
    
    # - Exit from queue
    logger.info(f'Queue trigger for {config.Q_TRANSCRIPTIONS_TO_ANALYZE} finished processing a message: {json_message}')
    
  except Exception as e:
    logger.info(f"An error occurred while processing q-transcriptions-to-analyze: {e}")
  
