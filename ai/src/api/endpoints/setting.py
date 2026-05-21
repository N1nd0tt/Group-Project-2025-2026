from http.client import HTTPException

import asyncpg
from fastapi import APIRouter
from fastapi.params import Depends

from src.db.db import get_db_pool
from src.db.models import SettingsDB
from src.models.setting import GenerateSettingResponse, GenerateSettingRequest, Setting
from src.workflows.setting_graph import setting_app

router = APIRouter(prefix="/setting", tags=["World Generation"])


@router.post("/generate", response_model_exclude={"context"})
async def generate_setting(
        request: GenerateSettingRequest,
        pool: asyncpg.Pool = Depends(get_db_pool)) -> GenerateSettingResponse:
    # Invoke the AI workflow
    ai_response = await setting_app.ainvoke(request.model_dump())
    print("AI Response:", ai_response)  # Debugging output

    # Validate AI response
    if "setting_id" not in ai_response:
        raise HTTPException(status_code=500, detail="AI response missing 'setting_id'")

    # Create the setting
    setting = Setting.model_validate(ai_response)
    settings_db = SettingsDB(pool)
    await settings_db.create_setting(
        setting_id=ai_response["setting_id"],
        setting=setting
    )

    return GenerateSettingResponse(
        setting_id=ai_response["setting_id"],
        setting=setting
    )


@router.get("/{setting_id}")
async def generate_locations(setting_id: str, pool: asyncpg.Pool = Depends(get_db_pool)) -> Setting:
    setting_db = SettingsDB(pool)
    setting = await setting_db.get_setting(setting_id)
    return setting
