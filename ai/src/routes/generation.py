from fastapi import APIRouter, HTTPException
from src.models import (
    WorldGenerationRequest,
    WorldGenerationResponse,
    CharacterGenerationRequest,
    CharacterGenerationResponse
)
    CharacterGenerationRequest,
    CharacterGenerationResponse
)
from fastapi import Request

router= APIRouter(prefix="/gen", tags=["Generation"])


@ router.post("/world", response_model=WorldGenerationResponse)
async def create_world(request: WorldGenerationRequest, app_req: Request):
    try:
        dm= app_req.app.state.dm
        response= await dm.generate_world(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@ router.post("/character", response_model=CharacterGenerationResponse)
async def create_character(request: CharacterGenerationRequest, app_req: Request):
    try:
        dm = app_req.app.state.dm
        response = await dm.generate_character(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
