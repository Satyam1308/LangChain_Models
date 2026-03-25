from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

documents = [
    "The cat sat on the mat.",
    "The dog chased the ball.",
    "The bird flew in the sky.",
    "The fish swam in the water.",
    "The rabbit hopped in the grass.",
    "The snake slithered on the ground.",
    "The lion roared in the jungle.",
    "The tiger prowled in the forest.",
    "The elephant trumpeted in the savanna.",
    "The monkey swung in the trees.",
]

embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

result = embedding.embed_documents(documents)

print(str(result))