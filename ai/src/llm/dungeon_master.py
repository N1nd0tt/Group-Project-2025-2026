import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from src.models import (
    WorldGenerationRequest,
    WorldGenerationResponse,
    GameActionRequest,
    GameActionResponse,
    GameState
)


def get_model(temperature: float = 0.7):
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=temperature,
        convert_system_message_to_human=True
    )


async def generate_world(request: WorldGenerationRequest) -> WorldGenerationResponse:
    llm = get_model(request.temperature)

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


async def process_game_action(request: GameActionRequest) -> GameActionResponse:
    llm = get_model(request.temperature)

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

    # We combine the system prompt + history + latest input
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

    # Ensure internal logic handles missing state fields gracefully if LLM omits them
    updated_state_data = result.get("updated_state", {})

    # Merge with old state if partial, or just take new state
    # For simplicity, we assume the LLM provides a critical update or we fallback to current
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
