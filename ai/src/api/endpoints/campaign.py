import asyncpg
from fastapi import APIRouter, Depends

from src.db.db import get_db_pool
from src.db.models import CampaignsDB
from src.models.campaign import CampaignDeleteRequest, CampaignCreateRequest, Campaign

router = APIRouter(prefix="/campaign", tags=["Campaign Management"])


@router.post("/")
async def create_campaign(request: CampaignCreateRequest, pool: asyncpg.Pool = Depends(get_db_pool)):
    campaigns_db = CampaignsDB(pool)
    campaign = Campaign(
        id=request.campaign_id,
        owner_id=request.owner_id,
        setting_id=request.setting_id,
        name=request.name
    )
    await campaigns_db.create_campaign(campaign)


@router.get("/{campaign_id}")
async def get_campaign(campaign_id: str, pool: asyncpg.Pool = Depends(get_db_pool)) -> Campaign:
    campaigns_db = CampaignsDB(pool)
    campaign = await campaigns_db.get_campaign(campaign_id)
    return Campaign.model_validate(campaign)

# @router.post("/{campaign_id}/chat")
# async def chat(campaign_id: str, request: str):
#     pass

# @router.post("/{campaign_id}/delete")
# async def delete_campaign(campaign_id: str, request: CampaignDeleteRequest):
#     pass
