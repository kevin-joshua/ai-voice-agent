import os
from google import  genai



class IntentEngine:

    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


    async def extract_intent(self, text:str, language:str):
      prompt = f"Detect intent from the following {language} text:\n{text}\nIntent:"
      response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
      )
      intent = response.text
      print(intent)
      return intent 
    
    async def generate_response(self, intent:str, language:str):
       prompt = f"Generate a helpful customer support response for intent '{intent}' in {language}."
       response = self.client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
        )
       print(response.text)
       return response.text