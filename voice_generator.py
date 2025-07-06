import requests
import uuid
import os

def generate_voice(text: str) -> str:
    os.makedirs("static", exist_ok=True)
    
    # Call TTSMaker API
    url = "https://api.ttsmaker.com/v1/voice/speak"
    payload = {
        "Text": text,
        "VoiceType": "en_us_001",  # Try other types if needed
        "AudioFormat": "mp3",
        "Speed": 1.0
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if "download_url" in result:
            audio_data = requests.get(result["download_url"])
            filename = f"static/voice_{uuid.uuid4().hex}.mp3"
            with open(filename, "wb") as f:
                f.write(audio_data.content)
            return filename
        else:
            raise Exception("Voice generation failed. No download URL.")
    else:
        raise Exception(f"Voice API Error {response.status_code}: {response.text}")
