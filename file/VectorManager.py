from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid

class VectorManager:
    def __init__(self,host="", port=6333,collection="",dim=768,api_key=""):
        self.client = QdrantClient(
        url=f"https://{host}:{port}",
        api_key=api_key,
        )
        self.dim = dim
        self.collection = collection

    def add_vector(self,data,metadata):
        id_ = str(uuid.uuid4())
        metadata["id"] = id_
        self.client.upsert(
        collection_name=self.collection,
        points=[
            PointStruct(
                    id=id_,
                    vector=data,
                    payload=metadata
            )
        ]
        )

    def search(self, query_vector):
        hits = self.client.search(
        collection_name=self.collection,
        query_vector=query_vector,
        limit=5
        )
        return hits