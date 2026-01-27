from typing import TypedDict
from pydantic import BaseModel, Field
from src.models.setting import Region, BasicInfo, Society


class Location(BaseModel):
    name: str = Field(..., description="The name of the location")
    type: str = Field(..., description="The type of the location (e.g., city, dungeon, forest)")
    atmosphere: str = Field(..., description="The atmosphere or mood of the location")
    points_of_interest: list[str] = Field(..., description="List of points of interest in the location")
    description: str = Field(...,
                             description="A brief description of the location")


class LocationsState(TypedDict):
    region: Region
    number_of_locations: int
    world: BasicInfo
    society: Society
    locations: list[Location]
