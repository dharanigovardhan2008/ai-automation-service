from fastapi import APIRouter
from app.models.schemas import ReplyRequest, ReplyResponse
from app.services.ai_service import ask_gemini

router = APIRouter()

@router.post("/classify-reply", response_model=ReplyResponse)
def classify_reply(data: ReplyRequest):
    prompt = f"""
    You are a CRM reply classifier.
    Lead Name: {data.name}
    Their Reply: {data.reply}

    Classify their interest level and suggest next action.
    Reply in this exact format:
    Interest: High/Medium/Low
    Action: one line action to take
    """
    result = ask_gemini(prompt)
    lines = result.strip().split("\n")
    interest = lines[0].replace("Interest:", "").strip()
    action = lines[1].replace("Action:", "").strip()
    return {"interest_level": interest, "action": action}