from langgraph.graph import StateGraph
from ai.src.llm import llm
from src.models.location import LocationsState
from src.nodes.location import LocationsGenerationNodes

nodes = LocationsGenerationNodes(llm)
workflow = StateGraph(LocationsState)

workflow.add_node("generate", nodes.generate_locations)

workflow.set_entry_point("generate")
workflow.set_finish_point("generate")

locations_app = workflow.compile()
