from langgraph.constants import START, END
from langgraph.graph import StateGraph
from ai.src.nodes.setting import SettingGenerationNodes
from ai.src.llm import llm
from ai.src.models.setting import SettingState

nodes = SettingGenerationNodes(llm)
workflow = StateGraph(SettingState)

workflow.add_node("basic_info", nodes.generate_basic_info)
workflow.add_node("lore", nodes.generate_lore)
workflow.add_node("geography", nodes.generate_geography)
workflow.add_node("society", nodes.generate_society)

workflow.add_edge("basic_info", "lore")
workflow.add_edge("lore", "geography")
workflow.add_edge("geography", "society")
workflow.add_edge(START, "basic_info")
workflow.add_edge("society", END)

setting_app = workflow.compile()
