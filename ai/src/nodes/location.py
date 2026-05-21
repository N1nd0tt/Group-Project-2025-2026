import json
from langchain_google_genai import ChatGoogleGenerativeAI
from src.models.location import LocationsState, Location


class LocationsGenerationNodes:
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.structured_llm = llm.with_structured_output(Location)

    async def generate_locations(self, state: LocationsState) -> LocationsState:
        context = {
            "basic_info": state['world'].model_dump_json(),
            "society": state['society'].model_dump_json(),
        }

        prompt = f"""
        You are a Dungeon Master.
        Based on the following Setting context, generate {state.get('number_of_locations', 1)} detailed locations for a location in the provided region.
        
        REGION CONTEXT:
        {state['region'].model_dump_json()}
        
        SETTING CONTEXT:
        {context}
        
        Provide descriptions, atmosphere, and points of interest.
        All locations should fit within the context of the world, society and region provided.
        All locations should be unique and connected between each other (if multiple locations are generated).
        """

        response = await self.structured_llm.ainvoke(prompt)
        return {"locations": response.locations}
