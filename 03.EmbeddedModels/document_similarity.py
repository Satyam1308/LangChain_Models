from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

documents = [
    "Virat Kohli is a great batsman. He is known for his aggressive style of play. He is a right-handed batsman. His favourite shot is cover drive. His networth is 10000 million dollars.",
    "Rohit Sharma is a great batsman. He is known for his elegant style of play. He is a right-handed batsman. His favourite shot is pull shot. His networth is 1500 million dollars.",
    "Sachin Tendulkar is a great batsman. He is known for his classical style of play. He is a right-handed batsman. His favourite shot is straight drive. His networth is 20000 million dollars.",
]
query = "Tell me about the Virat Kohli"

doc_embedding = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)


result = cosine_similarity([query_embedding], doc_embedding)[0]

index, score = sorted(list(enumerate(result)), key=lambda x: x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is: ",score)
