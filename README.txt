English Speaking Coach - A Local English Speaking Coaching System

Project Introduction: This project is a locally running English speaking practice system that combines Whisper (speech recognition) and a local LLM (such as llama3) to enable instructional dialogues. Users can engage in natural English conversations with an AI teacher via a web interface. The system features real-time speech recognition, speech synthesis, grammar correction, and continuous conversation capabilities.


Core Functions:

- Automatically detects silence to start/end recording for seamless voice input.

- Whisper model for English speech recognition, forcing English mode to avoid misrecognition.

- LLM simulates a C1-level English teacher based on prompts, providing grammar explanations and dialogue guidance.

- Edge-TTS converts AI responses into voice playback, enhancing the interactive experience.

- Supports contextual memory, simulating natural conversational rhythm.

- All models and audio files run locally, ensuring data privacy and security.


Dependencies:

- Python >= 3.9

- Browser supports Web Audio API (Chrome or Edge recommended)

- Local deployment and running of llama3 or a compatible model in Ollama.


Usage:

1. Install dependencies:

pip install -r requirements.txt

2. Run the service in Terminal:

python app.py

3. Access via browser:

http://127.0.0.1:5000


Directory Structure:

- app.py: Main entry point for Flask service

- tts.py: Speech synthesis module (used for...) edge-tts)

- stt.py: Whisper speech recognition

- llm.py: Calls the local LLM model to process contextual dialogue

- config.json: Parameter settings (speech, model, etc.)

- prompts.json: Teacher prompt word templates

- static/: Stores the generated audio file (audio_reply.mp3)

- templates/: Web page HTML templates


Group distribution for the project:
- Songdi: 
- Rachel:
- Jan: 
- Jolein: 
