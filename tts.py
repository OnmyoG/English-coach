
import asyncio
from edge_tts import Communicate
import pygame
import time
import os

VOICES = {
    "en": "en-US-JennyNeural",
    "zh": "zh-CN-XiaoxiaoNeural"
}

def speak_text(text: str, lang: str = "en"):
    voice = VOICES.get(lang[:2], VOICES["en"])
    mp3_file = "output.mp3"

    # Delete the old file if it exists to avoid permission issues
    if os.path.exists(mp3_file):
        try:
            os.remove(mp3_file)
        except PermissionError:
            print("Cannot overwrite output.mp3 — file is in use.")
            return

    async def _synthesize():
        communicate = Communicate(text=text, voice=voice)
        await communicate.save(mp3_file)

    asyncio.run(_synthesize())

    # Initialize pygame mixer to play MP3
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.2)

    pygame.mixer.music.stop()
    pygame.mixer.quit()
