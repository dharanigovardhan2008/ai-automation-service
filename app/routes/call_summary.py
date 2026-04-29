from fastapi import APIRouter
from app.models.schemas import CallSummaryRequest, CallSummaryResponse
from app.services.ai_service import ask_gemini

router = APIRouter()

@router.post("/call-summary", response_model=CallSummaryResponse)
def call_summary(data: CallSummaryRequest):
    prompt = f"""
    You are a CRM call summary assistant.
    Lead Name: {data.name}
    Call Transcript: {data.call_transcript}

    Summarize this call and classify the lead status.
    Reply in this exact format:
    Summary: one line summary
    Status: Interested/Not Interested
    Next Action: one line next action
    """
    result = ask_gemini(prompt)
    lines = result.strip().split("\n")
    summary = lines[0].replace("Summary:", "").strip()
    status = lines[1].replace("Status:", "").strip()
    next_action = lines[2].replace("Next Action:", "").strip()
    return {"summary": summary, "status": status, "next_action": next_action}