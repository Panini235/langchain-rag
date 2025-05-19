import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_embedding():
    from langchain_ollama import OllamaEmbeddings
    embedder = OllamaEmbeddings(model="nomic-embed-text")
    text = "你好，欢迎使用 LangChain！"
    vector = embedder.embed_query(text)
    print("✅ 嵌入成功，维度：", len(vector))
    print("向量前5项：", vector[:5])


def test_file_embedding(file_path):
    from file.Embedder import Embedder
    from file.DocumentLoader import DocumentLoader
    DocumentLoader = DocumentLoader(file_path)
    Embedder = Embedder()
    docs = DocumentLoader.load()
    print(f"✅ 成功加载文档，共 {len(docs)} 页/段")

    for i, doc in enumerate(docs):
        print(f"--- 第 {i+1} 页 ---")
        print("内容：", doc.page_content[:100])
        print("元数据：", doc.metadata)
        vector = Embedder.embed(doc.page_content)
        print(f"✅ 向量维度：{len(vector)}")
        break

def test_qdrant_upload():
    from file.VectorManager import VectorManager
    from langchain_ollama import OllamaEmbeddings
    VectorManager = VectorManager()
    embedder = OllamaEmbeddings(model="nomic-embed-text")
    text = "你好，欢迎使用 LangChain！"
    vector = embedder.embed_query(text)
    # print(vector)
    metadata = {"content":"test for qdrant upload"}
    VectorManager.add_vector(vector,metadata,text)

def test_qdrant_search(text="我的名字是什么？"):
    from file.VectorManager import VectorManager
    from langchain_ollama import OllamaEmbeddings
    VectorManager = VectorManager()
    embedder = OllamaEmbeddings(model="nomic-embed-text")
    vector = embedder.embed_query(text)
    hits = VectorManager.search(query_vector=vector)
    # print(hits)
    context = ""
    for hit in hits:
        score = hit.score
        content = hit.payload.get("content", "")
        context += f"- 匹配度：{score:.4f}\n  内容：{content}\n\n"
    return context


def test_file_pipeline():
    from file.VectorManager import VectorManager
    from pipeline.file_pipeline import FilePipeline
    vector_manager = VectorManager()
    file_pipeline = FilePipeline(vector_manager)
    file_pipeline.run(r"")


def test_minio_upload():
    from minio import Minio
    client = Minio("127.0.0.1:9000",
        access_key="",
        secret_key="",
        secure=False
    )
    bucket_name = "langchain-test-bucket"
    file_path = r""
    filename = "test.pdf"
    client.fput_object(
        bucket_name, filename, file_path,
    )

def test_assistant():
    from file.ModelAssistant import ModelAssistant
    model_assistant = ModelAssistant()
    response = model_assistant.query_assistant(question="hello,what's my name", context="my name is panini")
    print(response)


def test_assistant_knowledgebase():
    from file.ModelAssistant import ModelAssistant
    model_assistant = ModelAssistant()
    question = "什么是LLMOps"
    context = test_qdrant_search(question)
    response = model_assistant.query_assistant(question=question, context=context)
    print(response)




if __name__ == "__main__":
    # test_embedding()
    # test_file_embedding(r"")
    # test_qdrant_upload()
    # test_file_pipeline()
    # time.sleep(20)
    # test_qdrant_search()
    # test_minio_upload()
    # test_assistant()
    test_assistant_knowledgebase()