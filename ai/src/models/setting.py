from typing import TypedDict
from pydantic import BaseModel, Field


class BasicInfo(BaseModel):
    name: str = Field(..., description="The name of the setting")
    genre: str = Field(..., description="The genre of the setting")
    theme: str = Field(..., description="The main theme or motif")
    tech_level: str = Field(..., description="The technological level of the setting")
    magic_level: str = Field(..., description="The role and level of magic in the setting")


class Faction(BaseModel):
    name: str = Field(..., description="The name of the faction")
    description: str = Field(...,
                             description="A brief description of the faction")


class WorldLore(BaseModel):
    history: str = Field(..., description="History of the world and story setup (3-5 sentences)")
    major_events: str = Field(..., description="Major historical events that shaped the world")
    current_state: str = Field(..., description="The current state of the world")
    factions: list[Faction] = Field(..., description="List of major factions")


class Region(BaseModel):
    name: str = Field(..., description="The name of the region")
    description: str = Field(...,
                             description="A brief description of the region")


class Geography(BaseModel):
    regions: list[Region] = Field(..., description="List of regions")
    start_region: str = Field(...,
                              description="Name of the starting region for the adventure")


class Society(BaseModel):
    culture: str = Field(..., description="Description of the culture")
    races: list[str] = Field(..., description="List of predominant races")
    religion: str = Field(..., description="The dominant religion")
    laws: str = Field(..., description="Overview of the legal system")
    magic_legality: str = Field(..., description="Status of magic in society")


class SettingState(TypedDict):
    setting_key: str
    context: str
    info: BasicInfo
    lore: WorldLore
    geography: Geography
    society: Society


class Setting(BaseModel):
    info: BasicInfo
    lore: WorldLore
    geography: Geography
    society: Society


class GenerateSettingRequest(BaseModel):
    setting_id: str = Field(..., description="Unique ID provided by the Main Backend")
    context: str = Field(..., description="User prompt or context for generation")


class GenerateSettingResponse(BaseModel):
    setting_id: str = Field(..., description="Unique ID provided by the Main Backend")
    setting: Setting = Field(..., description="Generated setting details")
