from fastapi import FastAPI
from pydantic import BaseModel
from script_generator import generate_script
from voice_generator import generate_voice
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧠 Static folder mount
app.mount("/static", StaticFiles(directory="static"), name="static")


# Request body ke liye model
class ScriptRequest(BaseModel):
    topic: str
    style: str


class VoiceRequest(BaseModel):
    script: str


# ✅ API to generate script
from script_generator import clean_script  # 👈 is line ko import section me add karo

@app.post("/generate-script")
def generate_script_api(req: ScriptRequest):
    script = generate_script(req.topic, req.style)
    cleaned = clean_script(script)
    return {
        "raw_script": script,
        "cleaned_script": cleaned
    }



# ✅ API to generate voice
@app.post("/generate-voice")
def generate_voice_api(req: VoiceRequest):
    audio_url = generate_voice(req.script)
    return {"audio_url": audio_url}
