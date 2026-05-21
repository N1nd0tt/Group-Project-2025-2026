import asyncpg
from fastapi import APIRouter, Depends, HTTPException

from src.db.db import get_db_pool
from src.db.models import CampaignsDB, SettingsDB, ChatMessagesDB
from src.models.campaign import CampaignDeleteRequest, CampaignCreateRequest, Campaign
from src.workflows.chat_graph import chat_app_compiled as chat_app

from src.models.setting import Setting
from src.models.chat import ChatMessage, ChatState

router = APIRouter(prefix="/campaign", tags=["Campaign Management"])

@router.post("/")
async def create_campaign(request: CampaignCreateRequest, pool: asyncpg.Pool = Depends(get_db_pool)):
    campaigns_db = CampaignsDB(pool)
    settings_db = SettingsDB(pool)

    # Check if the setting already exists
    existing_setting = await settings_db.get_setting(request.setting_id)
    if not existing_setting:
        # Create a default setting
        default_setting = Setting()  # Replace with appropriate default values
        await settings_db.create_setting(request.setting_id, default_setting)

    # Create the campaign
    campaign = Campaign(
        campaign_id=request.campaign_id,
        owner_id=request.owner_id,
        setting_id=request.setting_id,
        name=request.name
    )
    await campaigns_db.create_campaign(campaign)


@router.post("/{campaign_id}/chat")
async def chat(campaign_id: str, message: str, pool: asyncpg.Pool = Depends(get_db_pool)):
    campaigns_db = CampaignsDB(pool)
    settings_db = SettingsDB(pool)
    chat_messages_db = ChatMessagesDB(pool)

    # Retrieve campaign
    campaign = await campaigns_db.get_campaign(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    # Retrieve setting data for context
    setting = await settings_db.get_setting(campaign.setting_id)
    if not setting:
        raise HTTPException(status_code=404, detail="Setting not found")

    # Save user message to database
    await chat_messages_db.add_message(campaign_id, "user", message)

    # Fetch chat history
    history_records = await chat_messages_db.get_messages(campaign_id)
    chat_history = [ChatMessage(sender=record["sender"], content=record["content"]) for record in history_records]

    # Initialize the chat state with full history
    state = {
        "messages": chat_history,
        "setting": setting,
        "campaign": campaign,
        "next_action": None
    }

    # Run the chat workflow
    try:
        response_state = await chat_app.ainvoke(state)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

    # Extract the new AI response message
    response_message = response_state["messages"][-1]
    
    # Save AI message to database
    await chat_messages_db.add_message(campaign_id, response_message.sender, response_message.content)

    return {"response": response_message.content}

@router.put("/{campaign_id}")
async def update_campaign(campaign_id: str, request: CampaignCreateRequest, pool: asyncpg.Pool = Depends(get_db_pool)):
    campaigns_db = CampaignsDB(pool)

    # Проверяем существование кампании
    campaign = await campaigns_db.get_campaign(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    # Обновляем кампанию
    updated_campaign = Campaign(
        campaign_id=campaign_id,
        owner_id=request.owner_id,
        setting_id=request.setting_id,
        name=request.name
    )
    await campaigns_db.update_campaign(updated_campaign)
    return {"detail": "Campaign updated successfully"}


@router.post("/{campaign_id}/add_player")
async def add_player_to_campaign(campaign_id: str, player_id: str, pool: asyncpg.Pool = Depends(get_db_pool)):
    campaigns_db = CampaignsDB(pool)

    # Проверяем существование кампании
    campaign = await campaigns_db.get_campaign(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    # Добавляем игрока
    await campaigns_db.add_player_to_campaign(campaign_id, player_id)
    return {"detail": "Player added successfully"}

@router.delete("/{campaign_id}")
async def delete_campaign(campaign_id: str, pool: asyncpg.Pool = Depends(get_db_pool)):
    campaigns_db = CampaignsDB(pool)

    # Retrieve campaign
    campaign = await campaigns_db.get_campaign(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaign not found")

    # Delete the campaign
    await campaigns_db.delete_campaign(campaign_id)
    return {"detail": "Campaign deleted successfully"}