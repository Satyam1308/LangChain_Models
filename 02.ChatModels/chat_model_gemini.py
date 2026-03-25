from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model= 'gemini-3-flash-preview')

response =model.invoke("What is Deep Learning?")

print(response.text)