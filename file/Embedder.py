# pypdf langchain langchain_community python-docx unstructured markdown langchain_ollama exceptions
"""
https://blog.csdn.net/weixin_44217158/article/details/141931045 使用LangChain加载多种格式的文件

"""
from langchain_ollama import OllamaEmbeddings

class Embedder:
    def __init__(self, model_name="nomic-embed-text"):
        self.model = OllamaEmbeddings(model=model_name)

    def embed(self, text: str):
        return self.model.embed_query(text)



# if __name__ == '__main__':
#     file_name = r"D:\STUDY\CloudComputing\Essential\langchain\test\test.txt"
#     embedder = FileEmbedder(file_name)
#     data = embedder.file_loader()[0]
#     metadata = data.metadata
#     text = data.page_content
#     vector = embedder.embedd_file(text)
#     item = {
#         "vector": vector,
#         "metadata": metadata
#     }
#     print(item)