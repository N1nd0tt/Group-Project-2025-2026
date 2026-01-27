from langchain_google_genai import ChatGoogleGenerativeAI

from src.models.setting import SettingState, BasicInfo, Geography, Society, WorldLore


class SettingGenerationNodes:
    def __init__(self, llm: ChatGoogleGenerativeAI):
        self.llm = llm
        self.llm_basic_info = llm.with_structured_output(BasicInfo)
        self.llm_lore = llm.with_structured_output(WorldLore)
        self.llm_geography = llm.with_structured_output(Geography)
        self.llm_society = llm.with_structured_output(Society)

    async def generate_basic_info(self, state: SettingState) -> SettingState:
        prompt = f"You are a Dungeon Master. Based on the following context: {state.get('context', 'players not provide any context')}, generate a setting for new adventure."
        response = await self.llm_basic_info.ainvoke(prompt)
        return {"info": response}

    async def generate_lore(self, state: SettingState) -> SettingState:
        context = {
            "basic_info": state['info'].model_dump_json()
        }

        prompt = f"""
        You are a Dungeon Master. Based on the following setting context,
        generate world lore including history, major events, current state, and factions.

        SETTING CONTEXT (JSON):
        {context}
        """

        response = await self.llm_lore.ainvoke(prompt)
        return {"lore": response}

    async def generate_geography(self, state: SettingState) -> SettingState:
        context = {
            "basic_info": state['info'].model_dump_json(),
            "lore": state['lore'].model_dump_json()
        }

        prompt = f"""
        You are a Dungeon Master. Based on the following setting context, 
        generate the geography of the world including regions, and specify a starting region for the adventure.
        
        SETTING CONTEXT (JSON):
        {context}
        """

        response = await self.llm_geography.ainvoke(prompt)
        return {"geography": response}

    async def generate_society(self, state: SettingState) -> SettingState:
        context = {
            "basic_info": state['info'].model_dump_json(),
            "lore": state['lore'].model_dump_json(),
            "geography": state['geography'].model_dump_json()
        }

        prompt = f"""
        You are a Dungeon Master. Based on the following setting context,
        generate the society details including culture, races, religion, laws, and magic legality.
        
        SETTING CONTEXT (JSON):
        {context}
        """

        response = await self.llm_society.ainvoke(prompt)
        return {"society": response}
