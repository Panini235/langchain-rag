from langchain_community.document_loaders import PyPDFLoader, TextLoader, UnstructuredMarkdownLoader
from os import path


class DocumentLoader:
    loaders = {
        ".pdf": PyPDFLoader,
        ".md": UnstructuredMarkdownLoader,
        ".txt": TextLoader,
    }

    def __init__(self, file_path):
        self.file_path = file_path
        self.suffix = self.detect_suffix(file_path)
        if self.suffix not in self.loaders:
            raise ValueError(f"Unsupported file type: {self.suffix}")

    def detect_suffix(self, file_path):
        return path.splitext(file_path)[-1]

    def load(self):
        loader_class = self.loaders[self.suffix]
        if self.suffix == ".txt":
            loader = loader_class(self.file_path, encoding="utf-8")
        else:
            loader = loader_class(self.file_path)
        return loader.load()

