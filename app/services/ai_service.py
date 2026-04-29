from google import genai
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"AI service error: {str(e)}")