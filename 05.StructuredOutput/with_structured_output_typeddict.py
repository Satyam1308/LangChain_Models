from typing import TypedDict, Annotated, Literal, Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Review (TypedDict):
   summary: Annotated[str, "Please provide me a brief summary of the review"]
   sentiment: Annotated[Literal["negative", "positive", "neutral"], "Return the sentiment of the review either negative, positive or neutral"]
   rating: Annotated[Optional[int], "Return the rating of the review between 1 to 5"]

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("Very disappointed with this product. The quality is extremely poor and it stopped working within a few days. It doesn’t match the description at all. Totally not worth the money.")

print(result)    