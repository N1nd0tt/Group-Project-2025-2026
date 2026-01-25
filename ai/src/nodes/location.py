import json

from langchain_google_genai import ChatGoogleGenerativeAI

from src.models.location import LocationsState, GenerateLocationsResponse
from src.models.world import Society, Geography, BasicWorldInfo
from src.models.world import WorldState


class LocationsGenerationNodes:
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.structured_llm = llm.with_structured_output(GenerateLocationsResponse)

    async def generate_locations(self, state: LocationsState) -> LocationsState:
        prompt = f"""
        You are a Dungeon Master.
        Based on the following World information:
        - Basic Info: {json.dumps(state['world'])},
        - Society: {json.dumps(state['society'])},
        Generate {state.get('number_of_locations', 1)} detailed location description(s) for a location in the region: {json.dumps(state['region'])}.
        Provide descriptions, atmosphere, and points of interest.
        All locations should fit within the context of the world, society and region provided.
        All locations should be unique and connected between each other (if multiple locations are generated).
        """

        response = await self.structured_llm.ainvoke(prompt)
        return {"locations": response.locations}
