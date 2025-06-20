Here’s a full-fledged, professional-grade `README.md` for your **AI Voice Agent System** using Vapi, Deepgram, ElevenLabs, and OpenAI — built in Python with FastAPI:

---

```markdown
# 🎙️ AI Voice Agent System – PoC

A production-ready proof-of-concept AI voice assistant system that supports **inbound and outbound voice calls** with intelligent conversation handling, built using:

- [Vapi.ai](https://vapi.ai) – voice assistant infrastructure (calls, audio streaming)
- [Deepgram](https://deepgram.com) – real-time speech-to-text (STT)
- [ElevenLabs](https://elevenlabs.io) – text-to-speech (TTS)
- [OpenAI](https://platform.openai.com/) – intent extraction & response generation
- FastAPI (Python) – backend orchestration
- PostgreSQL/SQLite – ticket and transcript storage

---

## 🔧 Features

- ✅ Outbound voice calls to customers using Vapi
- ✅ Inbound call handling via webhook (with real-time STT)
- 🎤 Real-time audio streaming → Deepgram
- 🧠 Intent detection from transcript (via OpenAI)
- 🗣️ AI voice replies via ElevenLabs TTS
- 📝 Transcript & intent logging
- 🧪 Multi-language support (optional)
- 🚀 Fully modular + extensible backend

---

## 📁 Project Structure

```

ai-voice-agent/
├── app/
│   ├── main.py                     # FastAPI app entry
│   ├── routes/
│   │   └── vapi\_routes.py          # Webhook route for Vapi events
│   ├── services/
│   │   ├── vapi\_service.py         # Vapi integration: call, speak, stream
│   │   ├── deepgram\_streamer.py    # Real-time Deepgram STT handler
│   │   ├── tts\_service.py          # ElevenLabs TTS logic
│   │   └── intent\_service.py       # OpenAI-based intent extraction
│   └── models/
│       └── db.py                   # DB connection (SQLite/PostgreSQL)
├── requirements.txt
└── README.md

````

---

## 🚀 Quick Start

### 1. Clone this repo

```bash
git clone https://github.com/your-org/ai-voice-agent.git
cd ai-voice-agent
````

### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
VAPI_API_KEY=your_vapi_key
VAPI_ASSISTANT_ID=your_vapi_assistant_id
DEEPGRAM_API_KEY=your_deepgram_key
ELEVENLABS_API_KEY=your_elevenlabs_key
OPENAI_API_KEY=your_openai_key
TTS_VOICE_ID=elevenlabs_voice_id
```

### 4. Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## ☎️ Outbound Call Example

```bash
curl -X POST http://localhost:8000/call/start \
     -H "Content-Type: application/json" \
     -d '{"phone_number": "+1XXXXXXXXXX"}'
```

---

## 📡 Vapi Webhook Endpoint

Set this in your Vapi assistant settings:

```
https://yourdomain.com/webhook/vapi-events
```

✅ Handles:

* `media` audio streams (base64)
* `call.ended` to stop STT session

---

## 🧠 Intent Extraction Logic

Uses OpenAI to extract high-level intents like:

* “Schedule a callback”
* “Transfer to human”
* “Refund request”
* “Resolve issue”

You can extend `intent_service.py` to support your own logic.

---

## 🔊 Audio Format

* Vapi streams audio as base64-encoded `mulaw 8000Hz`
* Deepgram WebSocket is configured with:

  ```python
  LiveOptions(
    model="nova-3",
    encoding="mulaw",
    sample_rate=8000,
    channels=1
  )
  ```

---

## 🛠️ API Key Configuration in Vapi

When creating a **Private API Key**, set:

**Allowed Origins Regex**:

```
^https:\/\/([a-zA-Z0-9-]+\.)?yourdomain\.com\/?$
```

For dev/testing:

```
^http:\/\/localhost(:[0-9]+)?$
```

---

## 🧪 Test Flow

1. User receives an outbound call or calls your assistant.
2. Audio is streamed to Deepgram → transcript is generated.
3. Transcript → OpenAI → intent is extracted.
4. Reply text → ElevenLabs → audio URL.
5. Audio is sent back to the user using Vapi’s `/play` endpoint.

---

## ✅ Tech Stack

| Component     | Tool             |
| ------------- | ---------------- |
| Voice Infra   | Vapi.ai          |
| Transcription | Deepgram         |
| TTS           | ElevenLabs       |
| NLU / AI      | OpenAI (GPT-4)   |
| Backend       | FastAPI (Python) |
| DB            | SQLite/Postgres  |
| Auth/Config   | dotenv + HTTPS   |

---

## ✨ Future Improvements

* ✅ Live agent routing (via queue/ticket)
* ✅ Language detection & switching (Hindi, Tamil, etc.)
* ✅ Custom CRM API integrations
* ✅ Full analytics dashboard

---

## 🧑‍💻 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feat/my-feature`)
3. Commit your changes
4. Push and create a PR!

---

## 📜 License

MIT © \[Your Name or Organization]

---
