from langchain_community.llms.ollama import Ollama

from langchain_community.llms.ollama import Ollama
from langchain_community.llms.ollama import Ollama
import streamlit as st

st.title("Jarvis")
input_txt = st.text_input("Please enter the queries here.")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful AI assistant. Your name is Jarvis"),
        ("user", "user query:{query}")
    ]
)

llm = Ollama(model="llama2")  # Use the correct callable object from the ollama module
output_parser = StrOutputParser()

chain = prompt|llm | output_parser

if input_txt:
    st.write(chain.invoke({"query": input_txt}))