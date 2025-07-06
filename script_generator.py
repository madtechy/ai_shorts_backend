import google.generativeai as genai
import re

# ✅ Gemini API Key
genai.configure(api_key="AIzaSyBfXH-dvlYsqiSbU0mwzNHpSSf4TMj3PtA")
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Script generation with error handling
def generate_script(topic: str, style: str) -> dict:
    topics = [t.strip() for t in topic.split(",")]
    result = {}

    for t in topics:
        prompt = f"Write a 60-second video script in {style} style about: {t}"
        try:
            response = model.generate_content(prompt)
            if hasattr(response, "text") and response.text:
                result[t] = response.text
            else:
                result[t] = "❌ Failed to generate script for this topic."
        except Exception as e:
            print(f"❌ Error for topic '{t}':", e)
            result[t] = f"❌ Error occurred: {e}"

    return result

# ✅ (Optional) Clean script for TTS
def clean_script(raw_script: str) -> str:
    cleaned = re.sub(r"\*\*(.*?)\*\*", r"\1", raw_script)
    cleaned = re.sub(r"\d{1,2}-\d{1,2} seconds:.*?\n", "", cleaned)
    cleaned = re.sub(r"#+\s.*\n", "", cleaned)
    cleaned = cleaned.replace("\n", " ").strip()
    return cleaned
