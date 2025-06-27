import google.generativeai as genai

# Gemini API Key
genai.configure(api_key="AIzaSyBfXH-dvlYsqiSbU0mwzNHpSSf4TMj3PtA")

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_script(topic, style):
    prompt = f"Write a 60-second video script in {style} style about: {topic}"
    response = model.generate_content(prompt)
    return response.text
