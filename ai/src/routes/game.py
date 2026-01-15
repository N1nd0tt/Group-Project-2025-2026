from fastapi import APIRouter, HTTPException
from src.models import (
    GameActionRequest,
    GameActionResponse
)
from src.llm.dungeon_master import process_game_action

router = APIRouter(prefix="/dm", tags=["Dungeon Master"])


@router.post("/chat", response_model=GameActionResponse)
async def chat_interaction(request: GameActionRequest):
    try:
        response = await process_game_action(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
