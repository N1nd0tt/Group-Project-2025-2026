from typing import TypedDict

from pydantic import BaseModel, Field


class Faction(BaseModel):
    name: str = Field(..., description="The name of the faction")
    description: str = Field(...,
                             description="A brief description of the faction")


class Region(BaseModel):
    name: str = Field(..., description="The name of the region")
    description: str = Field(...,
                             description="A brief description of the region")


class Geography(BaseModel):
    regions: list[Region] = Field(..., description="List of regions")
    start_region: str = Field(...,
                              description="Name of the starting region for the adventure")


class BasicWorldInfo(BaseModel):
    name: str = Field(..., description="The name of the world")
    theme: str = Field(..., description="The main theme or motif")
    genre: str = Field(..., description="The genre of the world")
    story: str = Field(..., description="History of the world and story setup")


class Society(BaseModel):
    culture: str = Field(..., description="Description of the culture")
    races: list[str] = Field(..., description="List of predominant races")
    factions: list[Faction] = Field(..., description="List of major factions")
    religion: str = Field(..., description="The dominant religion")
    laws: str = Field(..., description="Overview of the legal system")
    magic_legality: str = Field(..., description="Status of magic in society")


class WorldState(TypedDict):
    context: str
    world: BasicWorldInfo
    geography: Geography
    society: Society
    starting_hook: str


class GenerateWorldRequest(BaseModel):
    context: str


class GenerateWorldResponse(BaseModel):
    world: BasicWorldInfo
    geography: Geography
    society: Society
    starting_hook: str
