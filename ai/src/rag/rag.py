import os
import shutil
from typing import List
from src.rag.load_documents import get_dnd_srd_documents
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStoreRetriever


class RAGManager:
    def __init__(
            self,
            persist_directory: str = "ai/chromadb",
            collection_name: str = "dungeon_master_guide",
            model_name: str = "all-MiniLM-L6-v2"
    ):
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.formatted_persist_directory = os.path.abspath(persist_directory)

        self.embedding_function = HuggingFaceEmbeddings(model_name=model_name)

        if os.path.exists(self.formatted_persist_directory):
            self.vector_store = Chroma(
                collection_name=self.collection_name,
                embedding_function=self.embedding_function,
                persist_directory=self.formatted_persist_directory
            )
        else:
            docs = get_dnd_srd_documents()

            self.vector_store = Chroma.from_documents(
                collection_name=self.collection_name,
                documents=docs,
                embedding=self.embedding_function,
                persist_directory=self.formatted_persist_directory
            )

    def reload_db(self) -> None:
        self.vector_store.delete_collection()
        docs = get_dnd_srd_documents()

        self.vector_store = Chroma.from_documents(
            collection_name=self.collection_name,
            documents=docs,
            embedding=self.embedding_function,
            persist_directory=self.formatted_persist_directory
        )

    async def search(self, query: str, k: int = 3) -> List[Document]:
        return await self.vector_store.asimilarity_search(query, k=k)

    def get_retriever(self, k: int = 3) -> VectorStoreRetriever:
        return self.vector_store.as_retriever(search_kwargs={"k": k})


async def main():
    rag_manager = RAGManager()
    results = await rag_manager.search("What classes are available?")
    for doc in results:
        print(f"Source: {doc.metadata.get('source', 'Unknown')}\nContent: {doc.page_content}\n")


# Debug
if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
