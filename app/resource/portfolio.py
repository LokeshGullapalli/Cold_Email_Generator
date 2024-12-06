import os
import pandas as pd
import chromadb
from chromadb.config import Settings
import uuid

class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            current_dir = os.path.dirname(__file__)
            file_path = os.path.join(current_dir, "my_portfolio.csv")

        self.file_path = file_path
        self.data = pd.read_csv(self.file_path)

        # Configure ChromaDB to use DuckDB as the backend
        self.chroma_client = chromadb.PersistentClient(
            Settings(
                chroma_db_impl="duckdb",
                persist_directory="./db"  # Directory where DuckDB files are stored
            )
        )
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        # Add portfolio entries to ChromaDB if not already added
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        # Query ChromaDB to find relevant portfolio links
        if not skills:
            return []

        query_str = " ".join(skills)
        response = self.collection.query(query_texts=[query_str], n_results=2)

        metadatas = response.get("metadatas", [[]])[0]
        return [meta["links"] for meta in metadatas]
