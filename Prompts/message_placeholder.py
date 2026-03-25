from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
])

model = ChatOpenAI(model="gpt-4o-mini")

chat_history = []

# Load history
with open("chat_history.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("You:"):
            chat_history.append(HumanMessage(content=line.replace("You:", "").strip()))
        else:
            chat_history.append(AIMessage(content=line.strip()))

question = input("You: ")

chain = chat_template | model

response = chain.invoke({
    "chat_history": chat_history,
    "question": question
})

print("AI:", response.content)

# Update history
chat_history.append(HumanMessage(content=question))
chat_history.append(AIMessage(content=response.content))

print(chat_history)