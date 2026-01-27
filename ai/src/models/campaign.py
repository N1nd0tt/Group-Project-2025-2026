from typing import Literal, Optional

from pydantic import BaseModel
from src.models.location import Location, Region


class CurrentLocation(BaseModel):
    location: Location
    region: Region


class Player(BaseModel):
    id: str
    name: str
    role: str


class Quest(BaseModel):
    title: str
    description: str
    status: Literal["active", "completed", "failed"]


class CampaignState(BaseModel):
    players: list[Player]
    current_location: CurrentLocation
    quests: list[Quest]


class Campaign(BaseModel):
    campaign_id: str
    owner_id: str
    setting_id: str
    name: str
    campaign_state: Optional[CampaignState] = None


class CampaignCreateRequest(BaseModel):
    owner_id: str
    campaign_id: str
    setting_id: str
    name: str


class CampaignDeleteRequest(BaseModel):
    owner_id: str
