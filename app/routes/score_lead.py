from fastapi import APIRouter
from app.models.schemas import LeadRequest, LeadResponse
from app.services.ai_service import ask_gemini

router = APIRouter()

@router.post("/score-lead", response_model=LeadResponse)
def score_lead(lead: LeadRequest):
    prompt = f"""
    You are a CRM lead scoring assistant.
    Lead Name: {lead.name}
    Phone: {lead.phone}
    Message: {lead.message}

    Based on this, classify the lead as Hot, Warm, or Cold.
    Reply in this exact format:
    Score: Hot/Warm/Cold
    Reason: one line reason
    """
    result = ask_gemini(prompt)
    lines = result.strip().split("\n")
    score = lines[0].replace("Score:", "").strip()
    reason = lines[1].replace("Reason:", "").strip()
    return {"score": score, "reason": reason}