# backend.py

# Step 1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List, Literal
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    task_type: Literal["chat", "transcription", "moderation"]
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Step 2: Setup FastAPI App
app = FastAPI(title="Multi-Task AI Agent API")

ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini"
]

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model."}

    # Task Routing
    if request.task_type == "chat":
        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )
        return response

    elif request.task_type == "moderation":
        # Simulated moderation response
        return {"moderation_result": "✅ No harmful content found."}

    elif request.task_type == "transcription":
        # Simulated transcription placeholder
        return {"transcription_result": "🎤 [Transcription feature is under development.]"}

    else:
        return {"error": "Unsupported task type."}


# Step 3: Run App
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
