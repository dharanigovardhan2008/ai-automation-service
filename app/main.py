from fastapi import FastAPI
from app.routes import score_lead, generate_message, classify_reply, call_summary

app = FastAPI(title="Gridian AI Automation Service")

app.include_router(score_lead.router)
app.include_router(generate_message.router)
app.include_router(classify_reply.router)
app.include_router(call_summary.router)

@app.get("/")
def root():
    return {"status": "Gridian AI Service is Running 🚀"}