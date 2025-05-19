from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

class ModelAssistant:
    def __init__(self,host="http://localhost:11434",model_name="deepseek-r1:14b",):
        self.model_name = model_name
        self.host = host
        template = """Question: {question}
                    you are a helpful assistant, you can sue below context to answer user's question, but if you do not the answer,please say Sorry, I cannot answer this question
                    Context: {context}
        """
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model=self.model_name)


    def query_assistant(self,question,context):
        chain = self.prompt | self.model
        return chain.invoke({"question": question,"context": context})


    def context_query_assistant():
        pass