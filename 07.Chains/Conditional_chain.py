from langchain_core.runnables import RunnableBranch
from pydantic import Field
from typing import Literal
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field

# Load environment variables (ensure GOOGLE_API_KEY is set)
load_dotenv()

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Define an output parser to extract plain text responses from the LLM
parser = StrOutputParser()

# Define a Pydantic model to enforce structured sentiment classification
class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(description="The sentiment of the feedback")

# Create a Pydantic parser to convert LLM output into the Feedback class format
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# --- PROMPT TEMPLATES ---

# Prompt 1: The Classifier - Determines if feedback is positive or negative
# Uses structured output instructions via parser2.get_format_instructions()
prompt1 = PromptTemplate(
    template="Classify the sentiments of the following Product feedback text into positive or negative \n {feedback}\n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

# Prompt 2: Success Handler - Generates a response for positive feedback
prompt2 = PromptTemplate(
    template='Write an appropriate 2 line response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

# Prompt 3: Failure Handler - Generates a response for negative feedback
prompt3 = PromptTemplate(
    template='Write an appropriate 2 line response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# --- CHAINS ---

# Classifier Chain: Takes raw feedback -> LLM -> Pydantic object (Feedback)
classifier_chain = prompt1 | model | parser2

# Branch Chain (Conditional Routing):
# Checks the 'sentiment' property of the classifier's output.
# 1. If "Positive", it routes to prompt2 (Positive Response).
# 2. If "Negative", it routes to prompt3 (Negative Response).
# 3. Default case: Handles unexpected results.
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Invalid feedback")
)

# Combined Chain: First classifies, then branches based on the classification
chain = classifier_chain | branch_chain

# --- EXECUTION ---

# Test the chain with negative feedback
result = chain.invoke({
    "feedback": "I am very happy with the excellent smartphone."
})

print("Chain Result:")
print(result)

# Display the workflow graph for visualization (useful for understanding the flow)
print("\nChain Execution Graph:")
print(chain.get_graph().print_ascii())


