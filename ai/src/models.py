from pydantic import BaseModel, Field
from typing import List, Optional


class WorldGenerationRequest(BaseModel):
    theme: str = Field(..., description="The genre or theme of the world (e.g., 'Dark Fantasy', 'Sci-Fi Cyberpunk')")
    tone: str = Field(
        "neutral", description="The tone of the description (e.g., 'grim', 'humorous', 'mysterious')")
    temperature: float = Field(
        0.7, ge=0.0, le=1.0, description="Randomness of the generation")


class WorldGenerationResponse(BaseModel):
    world_name: str
    description: str
    key_features: List[str]


class ChatMessage(BaseModel):
    role: str = Field(..., pattern="^(user|assistant|system)$")
    content: str


class GameState(BaseModel):
    """Context information state to be passed back and forth"""
    world_context: Optional[str] = None
    inventory: Optional[List[str]] = None
    location: Optional[str] = None


class GameActionRequest(BaseModel):
    input_text: str = Field(...,
                            description="The player's command or dialogue")
    history: List[ChatMessage] = Field(
        default_factory=list, description="Chat history for context")
    game_state: Optional[GameState] = Field(
        None, description="Current known state of the game")
    temperature: float = Field(0.7, ge=0.0, le=1.0)


class GameActionResponse(BaseModel):
    response_text: str
    updated_state: GameState
