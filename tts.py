import json, os
import asyncio
from edge_tts import Communicate
import re

with open(os.path.join(os.path.dirname(__file__), "config.json"), "r", encoding="utf-8") as f:
    config = json.load(f)

voice = config.get("voice", "en-US-JennyNeural")
speech_speed = config.get("speech_speed", 0.95)


def clean_text_for_speech(text):
    text = re.sub(r"\*+", "", text)
    text = re.sub(r"[#>`~]", "", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def speak_text(text: str, output_path: str = "static/audio_reply.mp3"):
    cleaned = clean_text_for_speech(text)

    async def _speak():
        if os.path.exists(output_path):
            os.remove(output_path)
        communicate = Communicate(
            text=cleaned,
            voice=voice,
            rate=f"{int((speech_speed - 1) * 100)}%"
        )
        await communicate.save(output_path)

    asyncio.run(_speak())
