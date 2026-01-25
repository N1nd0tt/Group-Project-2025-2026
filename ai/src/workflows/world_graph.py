from langgraph.constants import START, END
from langgraph.graph import StateGraph
from ai.src.nodes.world import WorldGenerationNodes
from ai.src.llm.llm import llm
from ai.src.models.world import WorldState

nodes = WorldGenerationNodes(llm)
workflow = StateGraph(WorldState)

workflow.add_node("basic_info", nodes.generate_basic_info)
workflow.add_node("geography", nodes.generate_geography)
workflow.add_node("society", nodes.generate_society)
workflow.add_node("starting_hook", nodes.generate_starting_hook)

workflow.add_edge("basic_info", "geography")
workflow.add_edge("geography", "society")
workflow.add_edge("society", "starting_hook")
workflow.add_edge(START, "basic_info")
workflow.add_edge("starting_hook", END)

world_app = workflow.compile()
