from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

st.header("Chatbot")

# Input fields
role = st.selectbox("Choose role: ",["Frontend Developer","Backend Developer","Fullstack Developer","Data Scientist","Machine Learning Engineer"])
question = st.text_input("Enter your question: ")

# Chat prompt template
chat_template = ChatPromptTemplate([
    ("system","You are a helpful {role} assistant."),
    ("human","{question}"),
])

# Invoke the model with the chat history
if st.button("Submit"):
    chain = chat_template | model
    with st.spinner("Generating response..."):
        response = chain.invoke({"role":role,"question":question})
        st.write(response.content)

