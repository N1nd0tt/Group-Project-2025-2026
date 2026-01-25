from fastapi import APIRouter
from src.models.location import GenerateLocationsRequest, GenerateLocationsResponse
from src.models.world import GenerateWorldRequest, GenerateWorldResponse
from src.workflows.world_graph import world_app
from src.workflows.locations_graph import locations_app

router = APIRouter(prefix="/generate", tags=["World Generation"])


@router.post("/world", response_model_exclude={"context"})
async def generate_world(request: GenerateWorldRequest) -> GenerateWorldResponse:
    response = await world_app.ainvoke(request.model_dump())
    return response


@router.post("/locations")
async def generate_locations(request: GenerateLocationsRequest) -> GenerateLocationsResponse:
    response = await locations_app.ainvoke(request.model_dump())
    return GenerateLocationsResponse(locations=response['locations'])
