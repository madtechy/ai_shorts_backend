from gtts import gTTS
import uuid
import os


def generate_voice(text):
    os.makedirs("static", exist_ok=True)
    filename = f"static/voice_{uuid.uuid4().hex}.mp3"
    tts = gTTS(text)
    tts.save(filename)
    return filename
