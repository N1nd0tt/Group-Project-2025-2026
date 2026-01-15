from fastapi import APIRouter, HTTPException
from src.models import (
    WorldGenerationRequest,
    WorldGenerationResponse,
)
from src.llm.dungeon_master import generate_world

router = APIRouter(prefix="/gen", tags=["Generation"])


@router.post("/world", response_model=WorldGenerationResponse)
async def create_world(request: WorldGenerationRequest):
    try:
        response = await generate_world(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
