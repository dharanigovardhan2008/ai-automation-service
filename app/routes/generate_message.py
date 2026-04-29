from fastapi import APIRouter
from app.models.schemas import MessageRequest, MessageResponse
from app.services.ai_service import ask_gemini

router = APIRouter()

@router.post("/generate-message", response_model=MessageResponse)
def generate_message(data: MessageRequest):
    prompt = f"""
    You are a WhatsApp CRM message writer.
    Lead Name: {data.name}
    Business: {data.business}
    Lead Score: {data.score}

    Write a short, friendly, professional WhatsApp follow-up message
    for this lead. Keep it under 3 sentences.
    Reply with only the message, nothing else.
    """
    result = ask_gemini(prompt)
    return {"message": result.strip()}