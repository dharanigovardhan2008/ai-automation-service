from pydantic import BaseModel

# Lead Scoring
class LeadRequest(BaseModel):
    name: str
    phone: str
    message: str

class LeadResponse(BaseModel):
    score: str  # Hot / Warm / Cold
    reason: str

# Message Generation
class MessageRequest(BaseModel):
    name: str
    business: str
    score: str

class MessageResponse(BaseModel):
    message: str

# Reply Classification
class ReplyRequest(BaseModel):
    name: str
    reply: str

class ReplyResponse(BaseModel):
    interest_level: str  # High / Medium / Low
    action: str

# Call Summary
class CallSummaryRequest(BaseModel):
    name: str
    call_transcript: str

class CallSummaryResponse(BaseModel):
    summary: str
    status: str  # Interested / Not Interested
    next_action: str