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
