import tempfile
from typing import List
from langchain_core.documents import Document
from langchain_community.document_loaders import GitLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

REPO_URL = "https://github.com/oldmanumby/DND.SRD.Wiki"


def custom_file_filter(file_path: str) -> bool:
    if not file_path.endswith(".md"):
        return False

    path_lower = file_path.lower()
    parts = path_lower.split('/')

    file_name = parts[-1]
    folders = parts[:-1]

    ignored_files = [
        "changelog.md",
        "legal.md",
        "readme.md"
    ]

    if file_name in ignored_files:
        return False

    for folder in folders:
        if "(alt)" in folder:
            return False

    return True


def get_dnd_srd_documents(repo_url: str = REPO_URL) -> List[Document]:
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    markdown_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on)
    recursive_splitter = RecursiveCharacterTextSplitter.from_language(
        language="markdown",
        chunk_size=1000,
        chunk_overlap=100,
        add_start_index=True
    )

    final_documents = []

    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"Cloning repository to {temp_dir}")

        loader = GitLoader(
            clone_url=repo_url,
            repo_path=temp_dir,
            branch="main",
            file_filter=custom_file_filter
        )

        raw_docs = loader.load()
        print(f"Loaded {len(raw_docs)} files.")

        md_header_splits = []
        for doc in raw_docs:
            splits = markdown_splitter.split_text(doc.page_content)
            for split in splits:
                combined_metadata = {**doc.metadata, **split.metadata}
                split.metadata = combined_metadata

                header_context = " > ".join([
                    split.metadata.get(h, "")
                    for h in ["Header 1", "Header 2", "Header 3"]
                    if h in split.metadata
                ])

                if header_context:
                    split.page_content = f"{header_context}\n{split.page_content}"

                md_header_splits.append(split)

        final_documents = recursive_splitter.split_documents(md_header_splits)

    return final_documents


# Debug
"""
if __name__ == "__main__":
    docs = get_dnd_srd_documents()

    if docs:
        print("\n--- Przykładowy Dokument ---")
        print(f"Treść: {docs[0].page_content[:100]}...")
        print(f"Metadane: {docs[0].metadata}")
"""
