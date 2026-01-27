from fastapi import APIRouter
from src.api.endpoints import setting, campaign

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(setting.router)
api_router.include_router(campaign.router)
