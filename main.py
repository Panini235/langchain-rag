from flask import Flask, request, jsonify
import os
from minio import Minio
from file.ModelAssistant import ModelAssistant
from pipeline.file_pipeline import FilePipeline
from file.MinioManager import MinioManager
from file.Embedder import Embedder
from file.VectorManager import VectorManager
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = Minio("127.0.0.1:9000",
        access_key="o1yVKM6GkH8LmaNOVtoC",
        secret_key="O1f3l5wtMrxd3jfsEfOYfdCMws6aTSbOgv7br0H4",
        secure=False
    )
bucket_name = "langchain-test-bucket"

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/upload", methods=['POST'])
def upload():
    minio_manager = MinioManager()
    file = request.files.get('file')
    filename = file.filename
    file_bytes = file.read()
    text = file_bytes.decode('utf-8')
    print(text)
    file_length = len(file_bytes)
    file.stream.seek(0)
    if file:
        minio_manager.put_stream_object(file, file_length)
        return jsonify({'message': f'{filename} 上传成功'}), 200
    else:
        return jsonify({'message': f'{filename} 上传失败'}), 502

@app.route("/embedd", methods=['POST'])
def embedding_text():
    file_pipeline = FilePipeline()
    filename = request.json.get('filename')
    minio_manager = MinioManager()
    file_path = minio_manager.get_object(filename)
    file_pipeline.run(file_path)
    return jsonify({'message': f'{filename} 嵌入成功'}), 200




@app.route("/query", methods=['POST'])
def query():
    embedder = Embedder()
    model_assistant = ModelAssistant(model_name="gemma2:2b")
    vector_manager = VectorManager()
    question = request.json.get("question")
    vector = embedder.embed(question)
    hits = vector_manager.search(query_vector=vector)
    # print(hits)
    context = ""
    for hit in hits:
        score = hit.score
        content = hit.payload.get("content", "")
        context += f"- 匹配度：{score:.4f}\n  内容：{content}\n\n"
    response = model_assistant.query_assistant(question=question, context=context)
    return {"response": response}


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8081)