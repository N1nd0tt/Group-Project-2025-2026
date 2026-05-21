import operator
from typing import List, Any, TypedDict, Optional, Annotated
from pydantic import BaseModel

class ChatMessage(BaseModel):
    sender: str
    content: str

class ChatState(TypedDict):
    messages: Annotated[List[ChatMessage], operator.add]
    setting: Any
    campaign: Any
    next_action: Optional[str]