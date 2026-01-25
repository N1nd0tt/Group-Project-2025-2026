from langchain_core.tools import tool, StructuredTool
from ai.src.rag import RAGManager


def create_search_tool(rag_manager: RAGManager):
    @tool
    async def search_game_knowledge(query: str) -> str:
        """
        Search the Dungeons And Dragons knowledge database for relevant information and game rules.
        Args:
            query (str): The search query.
        Returns:
            str: The search results formatted as a string.
        """
        print("tool used")
        results = await rag_manager.search(query)

        if not results:
            return "No relevant documents found."

        context = "\n\n".join(
            [f"Source: {doc.metadata.get('source', 'Unknown')}\nContent: {doc.page_content}" for doc in results])
        return context

    return search_game_knowledge
