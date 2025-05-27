import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

def ask_gemini(prompt: str) -> str:
    try:
        model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Gemini API error: {str(e)}")
