import pandas as pd
import chromadb
from chromadb.config import Settings
import uuid
import os

class Portfolio:
    def __init__(self, file_path=None):
        if file_path is None:
            current_dir = os.path.dirname(__file__)
            file_path = os.path.join(current_dir, "my_portfolio.csv")

        self.file_path = file_path
        self.data = pd.read_csv(self.file_path)

        # Use the newer Chroma client configuration without `chroma_db_impl`.
        # Just specify `persist_directory`, Chroma defaults to duckdb+parquet.
        self.chroma_client = chromadb.Client(
            Settings(
                persist_directory="./chroma_data"  # a new directory name
            )
        )

        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if self.collection.count() == 0:
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["Techstack"]],
                    metadatas={"links": row["Links"]},
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        if not skills:
            return []

        query_str = " ".join(skills)
        response = self.collection.query(query_texts=[query_str], n_results=2)
        metadatas = response.get("metadatas", [[]])[0]
        return [meta["links"] for meta in metadatas]
