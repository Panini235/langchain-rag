from file.DocumentLoader import DocumentLoader
from file.TextChunker import TextChunker
from file.Embedder import Embedder
from file.VectorManager import VectorManager

class FilePipeline:
    def __init__(self):
        self.chunker = TextChunker(chunk_size=300, chunk_overlap=50)
        self.embedder = Embedder()
        self.vector_manager = VectorManager()

    def run(self, file_path: str):
        loader = DocumentLoader(file_path)
        documents = loader.load()

        for doc in documents:
            text = doc.page_content
            metadata = doc.metadata

            chunks = self.chunker.chunk_text(text)

            for chunk in chunks:
                vector = self.embedder.embed(chunk)
                chunk_metadata = metadata.copy()
                chunk_metadata["content"] = chunk
                self.vector_manager.add_vector(vector, chunk_metadata)
