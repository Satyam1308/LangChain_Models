from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# Initialize the ChatOpenAI model
model = ChatOpenAI()
user_input = input("You: ")
# Initialize the messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=user_input),
]

# Invoke the model with the messages
response = model.invoke(messages)

# Append the model's response to the messages
messages.append(AIMessage(content=response.content))

print("messages: ", messages)