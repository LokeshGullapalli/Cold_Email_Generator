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

        # Explicitly set chroma_api_impl to "local" and provide a fresh directory
        # Also specify tenant and database explicitly:
        self.chroma_client = chromadb.Client(
            Settings(
                chroma_api_impl="local",
                persist_directory="./chroma_data"
            ),
            tenant="default_tenant",
            database="default"
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
