from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model = 'gpt-4o', temperature=0.3, max_completion_tokens=10)

response = model.invoke("Who is the current prime minister of india?")

print(response.content)