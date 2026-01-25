from langchain_google_genai import ChatGoogleGenerativeAI

from src.models.location import Location
from src.models.world import WorldState, BasicWorldInfo, Geography, Society


class WorldGenerationNodes:
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.llm_basic_info = llm.with_structured_output(BasicWorldInfo)
        self.llm_geography = llm.with_structured_output(Geography)
        self.llm_society = llm.with_structured_output(Society)

    async def generate_basic_info(self, state: WorldState) -> WorldState:
        prompt = f"You are a Dungeon Master. Based on the following context: {state.get('context', 'players not provide any context')}, generate a world story for new adventure."
        response = await self.llm_basic_info.ainvoke(prompt)
        return {"world": response}

    async def generate_geography(self, state: WorldState) -> WorldState:
        prompt = f"""You are a Dungeon Master. Based on the following world info: Name: {state['world'].name}, Genre: {state['world'].genre}, 
        Theme: {state['world'].theme}, Story: {state['world'].story}, generate a few geographical regions for the world and specify a starting region for the adventure."""

        response = await self.llm_geography.ainvoke(prompt)
        return {"geography": response}

    async def generate_society(self, state: WorldState) -> WorldState:
        prompt = f"""You are a Dungeon Master. Based on the following world info: Name: {state['world'].name}, Genre: {state['world'].genre}, 
        Theme: {state['world'].theme}, Story: {state['world'].story}, generate details about the society"""

        response = await self.llm_society.ainvoke(prompt)
        return {"society": response}

    async def generate_starting_hook(self, state: WorldState) -> WorldState:
        prompt = f"""
        You are a Dungeon Master. Based on the following world info: 
        - Name: {state['world'].name}, 
        - Genre: {state['world'].genre}, 
        - Theme: {state['world'].theme}, 
        - Story: {state['world'].story}, 
        - Society: {state['society'].model_dump()} 
        Generate an engaging starting hook for the adventure. Do not use any text formatting like markdown just plain text"""

        response = await self.llm.ainvoke(prompt)
        return {"starting_hook": response.content}
