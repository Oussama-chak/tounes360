from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.agent import TOUNES360Agent

router = APIRouter()
agent = TOUNES360Agent()

class ChatRequest(BaseModel):
    message: str
    
class ChatResponse(BaseModel):
    response: str

@router.post("/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    """Chat with TOUNES360 AI agent"""
    try:
        response = agent.generate_response(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "agent": "TOUNES360", "mode": "gemini_only"}