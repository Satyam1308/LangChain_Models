from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
load_dotenv()

# Initialize the ChatOpenAI model
model = ChatOpenAI(model="gpt-4o-mini")

# Initialize the chat history
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

# Print the chatbot is ready message
print("Chatbot is ready! Type 'exit' or 'quit' to end the conversation.")

# Loop to get user input and generate response
while True:
    user_input = input("You: ")
    # Append the user input to the chat history
    chat_history.append(HumanMessage(content=user_input))
    # Break the loop if the user enters 'exit' or 'quit'
    if user_input in ["exit", "quit"]:
       break
    # Invoke the model with the chat history
    result = model.invoke(chat_history)
    # Append the model's response to the chat history
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print("chat_history: ", chat_history)
    