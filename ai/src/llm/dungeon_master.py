import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.messages import HumanMessage, AIMessage

from src.models import (
    WorldGenerationRequest,
    WorldGenerationResponse,
    GameActionRequest,
    GameActionResponse,
    GameState,
    CharacterGenerationRequest,
    CharacterGenerationResponse
)


class DungeonMaster:
    def __init__(self, model: str, temperature: float = 0.7):
        self.model_name = model
        self.default_temperature = temperature
        self._model_cache = {}

    def _get_model(self, temperature: float = None):
        if temperature is None:
            temperature = self.default_temperature

        if temperature not in self._model_cache:
            self._model_cache[temperature] = ChatGoogleGenerativeAI(
                model=self.model_name,
                temperature=temperature,
                convert_system_message_to_human=True
            )
        return self._model_cache[temperature]

    async def generate_world(self, request: WorldGenerationRequest) -> WorldGenerationResponse:
        llm = self._get_model(request.temperature)
        parser = JsonOutputParser(pydantic_object=WorldGenerationResponse)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert World Builder for a tabletop RPG. "
                       "Create a unique and engaging world setting based on the user's theme. "
                       "The tone should be {tone}. "
                       "Return the output strictly as JSON matching the requested structure."),
            ("user", "Theme: {theme}\n\n{format_instructions}")
        ])

        chain = prompt | llm | parser

        result = await chain.ainvoke({
            "theme": request.theme,
            "tone": request.tone,
            "format_instructions": parser.get_format_instructions()
        })

        return WorldGenerationResponse(**result)

    async def process_game_action(self, request: GameActionRequest) -> GameActionResponse:
        llm = self._get_model(request.temperature)

        # Construct history parameters
        history_messages = []
        for msg in request.history:
            if msg.role == "user":
                history_messages.append(HumanMessage(content=msg.content))
            elif msg.role == "assistant":
                history_messages.append(AIMessage(content=msg.content))

        # Prepare system context with game state
        state_desc = "No specific state info."
        if request.game_state:
            state_desc = f"""
            World Context: {request.game_state.world_context}
            Current Location: {request.game_state.location}
            Inventory: {request.game_state.inventory}
            """

        system_prompt = (
            "You are an AI Dungeon Master. Your role is to guide the player through an adventure.\n"
            "Describe the environment, control NPCs, and adjudicate the results of player actions.\n"
            "Be responsive to the player's tone, but maintain consistency with the world.\n"
            "Keep descriptions vivid but concise enough for a chat interface.\n"
            f"Current Game State:\n{state_desc}\n\n"
            "After responding to the player, analyze if any significant state changes happened "
            "(e.g., location change, item obtained). "
            "Strictly return your final response as a JSON object with two fields: 'response_text' (display to user) "
            "and 'updated_state' (the new state object)."
        )

        parser = JsonOutputParser(pydantic_object=GameActionResponse)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "{system_message}"),
            MessagesPlaceholder(variable_name="history"),
            ("user", "{input_text}\n\n{format_instructions}")
        ])

        chain = prompt | llm | parser

        result = await chain.ainvoke({
            "system_message": system_prompt,
            "history": history_messages,
            "input_text": request.input_text,
            "format_instructions": parser.get_format_instructions()
        })

        # Ensure internal logic handles missing state fields gracefully
        updated_state_data = result.get("updated_state", {})
        old_state = request.game_state or GameState()

        new_state = GameState(
            world_context=updated_state_data.get(
                "world_context", old_state.world_context),
            location=updated_state_data.get("location", old_state.location),
            inventory=updated_state_data.get("inventory", old_state.inventory)
        )

        return GameActionResponse(
            response_text=result["response_text"],
            updated_state=new_state
        )

    async def generate_character(self, request: CharacterGenerationRequest) -> CharacterGenerationResponse:
        llm = self._get_model(request.temperature)
        parser = JsonOutputParser(pydantic_object=CharacterGenerationResponse)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert RPG Character Creator. "
                       "Create a detailed character based on the user's specifications. "
                       "Return strictly JSON."),
            ("user", "Name: {name}\nRace: {race}\nClass: {character_class}\nLevel: {level}\n\n{format_instructions}")
        ])

        chain = prompt | llm | parser

        result = await chain.ainvoke({
            "name": request.name or "Random",
            "race": request.race or "Random",
            "character_class": request.character_class or "Random",
            "level": request.level,
            "format_instructions": parser.get_format_instructions()
        })

        return CharacterGenerationResponse(**result)
