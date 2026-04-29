# AI Automation Service — Gridian Technologies

AI-powered WhatsApp CRM backend service built with FastAPI and Gemini AI.

## What This Service Does
- Scores leads as Hot / Warm / Cold
- Generates personalised WhatsApp messages
- Classifies lead replies and detects interest level
- Summarises voice call transcripts

## Tech Stack
- Python 3.13
- FastAPI
- Google Gemini AI (gemini-2.5-flash)
- Pydantic
- Uvicorn

## How to Run

### 1. Clone the repository
git clone https://github.com/dharanigovardhan2008/ai-automation-service.git
cd ai-automation-service

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Add your API key
Create a .env file and add:
GEMINI_API_KEY=your_gemini_api_key_here

### 5. Start the server
python -m uvicorn app.main:app --reload

### 6. Open Swagger UI
http://localhost:8000/docs

## API Endpoints

### POST /score-lead
Scores a lead as Hot, Warm, or Cold.

Input:
{
  "name": "Ravi Kumar",
  "phone": "9876543210",
  "message": "I am interested in your product"
}

Output:
{
  "score": "Hot",
  "reason": "Lead expressed strong interest"
}

### POST /generate-message
Generates a personalised WhatsApp follow-up message.

Input:
{
  "name": "Ravi Kumar",
  "business": "Gridian Technologies",
  "score": "Hot"
}

Output:
{
  "message": "Hi Ravi, hope you're doing well!..."
}

### POST /classify-reply
Classifies a lead's reply and suggests next action.

Input:
{
  "name": "Ravi Kumar",
  "reply": "Yes I am interested, please send details"
}

Output:
{
  "interest_level": "High",
  "action": "Send detailed information"
}

### POST /call-summary
Summarises a voice call transcript.

Input:
{
  "name": "Ravi Kumar",
  "call_transcript": "Agent: Hi Ravi... Ravi: Yes interested..."
}

Output:
{
  "summary": "Ravi expressed strong interest...",
  "status": "Interested",
  "next_action": "Schedule follow-up demo call"
}

## Team
Python/AI Team — Gridian Technologies
