from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.chat_usecase import ChatUseCase
from app.infrastructure.llm.bedrock_client import BedrockClient

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    usecase = ChatUseCase(BedrockClient())
    reply = usecase.execute(request.message)
    return {"reply": reply}
