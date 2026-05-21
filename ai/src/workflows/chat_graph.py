from langgraph.constants import START, END
from langgraph.graph import StateGraph
from src.nodes.chat import ChatNodes
from src.llm import llm
from src.models.chat import ChatState

chat_nodes = ChatNodes(llm)

chat_app = StateGraph(ChatState)

# Add nodes
chat_app.add_node("process_message", chat_nodes.process_message)
chat_app.add_node("continue_story", chat_nodes.continue_story)
chat_app.add_node("create_enemy", chat_nodes.create_enemy)
chat_app.add_node("create_npc", chat_nodes.create_npc)
chat_app.add_node("perform_action", chat_nodes.perform_action)

# Add edges
chat_app.add_edge(START, "process_message")
chat_app.add_conditional_edges(
    "process_message",
    chat_nodes.decision,
    {
        "continue_story": "continue_story",
        "create_enemy": "create_enemy",
        "create_npc": "create_npc",
        "perform_action": "perform_action",
    }
)

chat_app.add_edge("continue_story", END)
chat_app.add_edge("create_enemy", END)
chat_app.add_edge("create_npc", END)
chat_app.add_edge("perform_action", END)

chat_app_compiled = chat_app.compile()