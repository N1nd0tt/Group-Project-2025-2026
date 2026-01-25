from typing import TypedDict

from pydantic import BaseModel, Field

from src.models.world import Region, BasicWorldInfo, Society


class Location(BaseModel):
    name: str = Field(..., description="The name of the location")
    type: str = Field(..., description="The type of the location (e.g., city, dungeon, forest)")
    atmosphere: str = Field(..., description="The atmosphere or mood of the location")
    points_of_interest: list[str] = Field(..., description="List of points of interest in the location")
    description: str = Field(...,
                             description="A brief description of the location")


class GenerateLocationsRequest(BaseModel):
    region: Region = Field(..., description="The region where the location is found")
    number_of_locations: int = Field(..., description="Number of locations to generate")
    world: BasicWorldInfo = Field(..., description="Information about the world in which the location exists")
    society: Society = Field(..., description="Details about the society in the world")


class GenerateLocationsResponse(BaseModel):
    locations: list[Location] = Field(..., description="The generated location details")


class LocationsState(TypedDict):
    region: Region
    number_of_locations: int
    world: BasicWorldInfo
    society: Society
    locations: list[Location]
