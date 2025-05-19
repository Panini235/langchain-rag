import './App.css';
import React, { useState } from 'react';

function QueryButton() {
  const [response, setResponse] = useState('');

  const handleClick = () => {
    fetch('http://localhost:8081/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: '我的名字是什么？' })
    })
      .then(res => res.json())
      .then(data => setResponse(data.response))
      .catch(err => {
        console.error('请求失败:', err);
        setResponse('请求失败');
      });
  };

  return (
    <div className='card'>
      <button onClick={handleClick}>Click to Query</button>
      <p>{response}</p>
    </div>
  );
}

function FileUploader({ setUploadedFilename }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (!file) {
      alert('请先选择一个文件');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('http://localhost:8081/upload', {
      method: 'POST',
      body: formData,
    })
      .then(response => response.json())
      .then(data => {
        console.log('上传成功:', data);
        alert('上传成功');
        setUploadedFilename(file.name); // 将文件名传递给 App 状态
      })
      .catch(error => {
        console.error('上传失败:', error);
        alert('上传失败');
      });
  };

  return (
    <div className='card'>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>上传文件</button>
    </div>
  );
}

function FileEmbedder({ filename }) {
  const [response, setResponse] = useState('');

  const handleClick = () => {
    if (!filename) {
      alert('请先上传文件');
      return;
    }

    fetch('http://localhost:8081/embedd', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ filename })
    })
      .then(res => res.json())
      .then(data => setResponse(data.message))
      .catch(err => {
        console.error('嵌入请求失败:', err);
        setResponse('嵌入请求失败');
      });
  };

  return (
    <div className='card'>
      <button onClick={handleClick}>嵌入文件</button>
      <p>{response}</p>
    </div>
  );
}

function QuestionForm() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('http://localhost:8081/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question })
    })
      .then(res => res.json())
      .then(data => setResponse(data.response))
      .catch(error => {
        console.error('请求失败:', error);
        setResponse('请求失败');
      });
  };

  return (
    <div className='card'>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="请输入问题"
        />
        <button type="submit">提交问题</button>
      </form>
      <p>响应：{response}</p>
    </div>
  );
}

function App() {
  const [uploadedFilename, setUploadedFilename] = useState('');

  return (
    <>
      <h1>LangChain-RAG-Test</h1>
      <QueryButton />
      <FileUploader setUploadedFilename={setUploadedFilename} />
      <FileEmbedder filename={uploadedFilename} />
      <QuestionForm />
    </>
  );
}

export default App;
