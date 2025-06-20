import logging
from deepgram import (
    DeepgramClient,
    LiveTranscriptionEvents,
    LiveOptions,
)
import base64
import json

# Setup logging
logger = logging.getLogger("deepgram_streamer")
logging.basicConfig(level=logging.INFO)

DEFAULT_LIVE_OPTIONS = LiveOptions(
    model="nova-3",
    encoding="mulaw",     # or "linear16" depending on source
    sample_rate=8000,     # Twilio/Vapi typically uses 8000Hz
    channels=1,
    punctuate=True,
)

class DeepgramCallStreamer:
    def __init__(self, on_transcript_callback=None, options: LiveOptions = DEFAULT_LIVE_OPTIONS):
        self.deepgram = DeepgramClient()
        self.dg_connection = self.deepgram.listen.websocket.v("1")
        self.started = False

        # Callback to handle transcripts
        self.handler = on_transcript_callback or self.default_handler

        # Attach transcript handler
        self.dg_connection.on(LiveTranscriptionEvents.Transcript, self._on_transcript)

        # Start connection
        self._start_connection(options)

    def _start_connection(self, options):
        if not self.dg_connection.start(options):
            raise RuntimeError("Failed to start Deepgram connection.")
        self.started = True
        logger.info("Deepgram connection started.")

    def _on_transcript(self, _, result, **kwargs):
        transcript = result.channel.alternatives[0].transcript
        if transcript:
            self.handler(transcript)

    def default_handler(self, transcript):
        print(f"📝 Transcript: {transcript}")

    def send_audio(self, audio_chunk: bytes):
        """Call this method to stream audio chunks to Deepgram"""
        if self.started:
            self.dg_connection.send(audio_chunk)

    def stop(self):
        """Call this when the call ends to close connection"""
        self.dg_connection.finish()
        logger.info("Deepgram connection closed.")






# Initialize Deepgram once per call
streamer = DeepgramCallStreamer(on_transcript_callback=lambda t: print(f"🔊 {t}"))

# When receiving an audio message from Twilio or Vapi WebSocket:
def handle_audio_event(message: str):
    event = json.loads(message)

    if event.get("event") == "media":
        # Decode audio from base64
        audio_b64 = event["media"]["payload"]
        audio_bytes = base64.b64decode(audio_b64)

        # Send to Deepgram
        streamer.send_audio(audio_bytes)

# When the call ends
def on_call_end():
    streamer.stop()


# websocket url for now -> mu law compressed    for twilio 
DG_WS_URL = "wss://api.deepgram.com/v1/listen?punctuate=true&encoding=mulaw&sample_rate=8000"