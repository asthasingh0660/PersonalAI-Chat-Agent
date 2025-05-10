# PersonalAI Chat

A modular chatbot system built with Python that can answer user questions, search the web when needed, and give smart, helpful replies. It uses LangGraph for orchestration, supports models from OpenAI and Groq, and is designed to easily extend with features like voice replies, webhooks, and voice assistant support using Twilio or Vapi

---

## 🚀 Features

- Chat with an AI agent via a local web interface.
- Modular architecture: `frontend.py`, `backend.py`, and `ai_agent.py` for separation of concerns.
- Environment variables managed via `.env` for secure API key handling.
- Pipenv used for dependency isolation and environment management.

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PersonalAI-Chat.git
cd PersonalAI-Chat/AgenticPersonalChat


2. Setup Environment
Install Pipenv if not installed:

pip install pipenv
Then install dependencies:

pipenv install

3. Add Your Environment Variables
Create a .env file (already included for structure) with your API keys and settings. Example:

OPENAI_API_KEY=your_openai_key
OTHER_API_KEYS=...

4. Run the App

pipenv run python backend.py
on another terminal -
	streamlit run frontend.py

🧠 Potential Future Use Cases
🎙️ 1. Speech Integration using gTTS
Add text-to-speech responses using Google Text-to-Speech:

from gtts import gTTS
import os

tts = gTTS(text="Hello there!", lang='en')
tts.save("response.mp3")
os.system("start response.mp3")

🧑‍💻 2. Voice Assistant with Twilio or VAPI
Transform this into a voice assistant by using:

Webhooks to receive and respond to voice calls.

WebSockets for real-time streaming interactions.

Integration Options:

Vapi SDK

Twilio Voice API

⚠️ Known Limitations
Some models (like GPT-4o Mini) now require a paid billing account with OpenAI. Ensure billing is set up to avoid access errors.

Some GoRQ-based models (like gpt-neo, gpt-j) may be deprecated or unsupported.

Always check the status of APIs and models you're using to avoid runtime issues.

🧰 Tech Stack
Python 3.10+

Pipenv for environment management

OpenAI GPT API

Flask / FastAPI (depending on your backend)

gTTS (optional, for speech)

📦 Folder Structure

AgenticPersonalChat/
│
├── ai_agent.py          # Main AI logic
├── backend.py           # Server-side code
├── frontend.py          # Interface / UI
├── Pipfile              # Dependency file
├── Pipfile.lock         # Exact versions
└── .env                 # API keys and config


📌 To Do / Enhancements
 Add speech input and output (STT + gTTS)

 Integrate with Twilio or Vapi

 Add multi-language support

 Host the app (e.g., Render, Railway, Vercel)

 Deploy with Docker

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---