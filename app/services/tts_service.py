import requests
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
import os 
from typing import IO
from io import BytesIO

load_dotenv()

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def generate_speech(text: str):
    response = elevenlabs.text_to_speech.convert(
      text=text,
      voice_id="JBFqnCBsd6RMkjVDRZzb",
      model_id="eleven_multilingual_v2",
      output_format="mp3_44100_128",

      voice_settings= VoiceSettings(
        stability=0.3,
        similarity_boost=1.0,
        style=0.0,
        use_speaker_boost=True,
        speed=1.0,
        ),
      )
    
    audio_stream = BytesIO()

    for chunk in response:
        if chunk: 
            audio_stream.write(chunk)
            
    audio_stream.seek(0)

    return audio_stream
    
  
