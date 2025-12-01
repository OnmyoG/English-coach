import whisper

model = whisper.load_model("base")

def transcribe_speech(file_path="temp.wav"):
    result = model.transcribe(file_path, language="en")
    return result['text'], result['language']
