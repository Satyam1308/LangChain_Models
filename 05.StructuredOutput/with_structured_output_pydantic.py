from typing import Optional
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

class Review (BaseModel):
   summary: str = Field(description="Please provide me a brief summary of the review")
   sentiment: str = Field(description="Return the sentiment of the review either negative, positive or neutral")
   rating: Optional[str] = Field(description="Return the rating of the review between 1 to 5", pattern=r"^[1-5]$")

structured_output = model.with_structured_output(Review)

result = structured_output.invoke("Very disappointed with this product. The quality is extremely poor and it stopped working within a few days. It doesn’t match the description at all. Totally not worth the money.")

print(result)    