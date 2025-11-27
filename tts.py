
import json, os
import asyncio
from edge_tts import Communicate
import pygame
import time

with open(os.path.join(os.path.dirname(__file__), "config.json"), "r", encoding="utf-8") as f:
    config = json.load(f)

voice = config.get("voice", "en-US-JennyNeural")
speech_speed = config.get("speech_speed", 0.8)

async def speak_text(text: str):
    mp3_file = "output.mp3"
    if os.path.exists(mp3_file):
        os.remove(mp3_file)
    communicate = Communicate(text=text, voice=voice, rate=f"{int((speech_speed - 1) * 100)}%")
    await communicate.save(mp3_file)

    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
