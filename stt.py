
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import queue
import threading
import sys

samplerate = 16000
channels = 1
model = whisper.load_model("base")
q = queue.Queue()

def audio_callback(indata, frames, time_info, status):
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def transcribe_speech():
    print("Recording... Press Enter again to stop:")

    recording_event = threading.Event()
    recording_event.set()

    def stop_on_enter():
        input()
        recording_event.clear()

    stopper = threading.Thread(target=stop_on_enter)
    stopper.start()

    audio = []
    with sd.InputStream(samplerate=samplerate, channels=channels, callback=audio_callback):
        while recording_event.is_set():
            try:
                data = q.get(timeout=0.1)
                audio.append(data)
            except queue.Empty:
                continue

    audio_np = np.concatenate(audio, axis=0)
    wav_file = "temp.wav"
    scipy.io.wavfile.write(wav_file, samplerate, audio_np)
    result = model.transcribe(wav_file)
    return result['text'], result['language']
