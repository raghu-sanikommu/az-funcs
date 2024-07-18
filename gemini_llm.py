import google.generativeai as genai


import config


genai.configure(api_key=config.GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel(config.GEMINI_LLM_MODEL_NAME)