from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.chatbot import router as chatbot_router

app = FastAPI(title="TOUNES360 AI Agent - Gemini Only", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(chatbot_router, prefix="/api/v1", tags=["chatbot"])

@app.get("/")
async def root():
    return {"message": "Welcome to TOUNES360 AI Agent API - Gemini Only Mode"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)