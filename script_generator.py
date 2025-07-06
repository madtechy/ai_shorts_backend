import google.generativeai as genai

# Gemini API Key config
genai.configure(api_key="AIzaSyBfXH-dvlYsqiSbU0mwzNHpSSf4TMj3PtA")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_script(topic: str, style: str) -> dict:
    """
    Generate scripts for multiple comma-separated topics
    :param topic: "AI, Robotics, Space"
    :param style: "funny", "educational", etc.
    :return: Dictionary with topic as key and script as value
    """
    topics = [t.strip() for t in topic.split(",")]
    result = {}

    for t in topics:
        prompt = f"Write a 60-second video script in {style} style about: {t}"
        response = model.generate_content(prompt)
        result[t] = response.text

    return result

import re

def clean_script(raw_script: str) -> str:
    """
    Remove markdown, timestamps, and formatting for clean TTS input.
    """
    # Remove markdown bold, italic
    cleaned = re.sub(r"\*\*(.*?)\*\*", r"\1", raw_script)
    
    # Remove timestamps like **0-5 seconds:**
    cleaned = re.sub(r"\d{1,2}-\d{1,2} seconds:.*?\n", "", cleaned)

    # Remove markdown headers like ## Title
    cleaned = re.sub(r"#+\s.*\n", "", cleaned)

    # Remove extra newlines
    cleaned = cleaned.replace("\n", " ").strip()

    return cleaned
