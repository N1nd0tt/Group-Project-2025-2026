from src.llm import llm

from src.models.chat import ChatMessage, ChatState


class ChatNodes:
    def __init__(self, llm):
        self.llm = llm

    async def process_message(self, state: ChatState) -> ChatState:
        # Анализируем сообщение и определяем следующий шаг
        last_message = state["messages"][-1]
        prompt = f"Player message: {last_message.content}\nBased on the campaign and setting, decide the next action. You MUST return EXACTLY ONE of the following keywords with no punctuation or additional text: continue_story, create_enemy, create_npc, perform_action."
        response = await self.llm.ainvoke(prompt)
        next_action = response.content.strip()
        
        # fallback to a default action if output is malformed
        if next_action not in ["continue_story", "create_enemy", "create_npc", "perform_action"]:
            next_action = "continue_story"
            
        return {"next_action": next_action}

    def decision(self, state: ChatState) -> str:
        # Determine the next node based on `state["next_action"]`
        action = state.get("next_action", "continue_story")
        if action in ["continue_story", "create_enemy", "create_npc", "perform_action"]:
            return action
        return "continue_story"

    async def continue_story(self, state: ChatState) -> ChatState:
        # Продолжение истории
        prompt = f"Continue the story based on the current state: {state}"
        response = await self.llm.ainvoke(prompt)
        return {"messages": [ChatMessage(sender="AI", content=response.content)]}

    async def create_enemy(self, state: ChatState) -> ChatState:
        # Создание врага
        prompt = f"Create an enemy based on the current state: {state}"
        response = await self.llm.ainvoke(prompt)
        return {"messages": [ChatMessage(sender="AI", content=response.content)]}

    async def create_npc(self, state: ChatState) -> ChatState:
        # Создание NPC
        prompt = f"Create an NPC based on the current state: {state}"
        response = await self.llm.ainvoke(prompt)
        return {"messages": [ChatMessage(sender="AI", content=response.content)]}

    async def perform_action(self, state: ChatState) -> ChatState:
        # Выполнение действия
        prompt = f"Perform an action based on the current state: {state}"
        response = await self.llm.ainvoke(prompt)
        return {"messages": [ChatMessage(sender="AI", content=response.content)]}