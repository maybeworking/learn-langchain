from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF/Llama3.1.gguf")

chain = prompt | model

chain.invoke({"question": "What is LangChain?"})