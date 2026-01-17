from fastapi import APIRouter, HTTPException
from src.models import (
    GameActionRequest,
    GameActionResponse
)
    GameActionResponse
)
from fastapi import Request


router= APIRouter(prefix="/dm", tags=["Dungeon Master"])


@ router.post("/chat", response_model=GameActionResponse)
async def chat_interaction(request: GameActionRequest, app_req: Request):
    try:
        dm= app_req.app.state.dm
        response= await dm.process_game_action(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
