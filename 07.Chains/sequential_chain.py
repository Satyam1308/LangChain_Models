from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()


# Prompt Template 1
prompt_template1 = PromptTemplate(
    template="Give me the brief summary on {topic}?",
    input_variables=["topic"]
)

# Prompt Template 2
prompt_template2 = PromptTemplate(
    template="Give me the 5 point summary from the following text.\n\n{formatted_message}",
    input_variables=["formatted_message"],
)

#Model1
model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#Model2
model2 = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Output Parser
parser = StrOutputParser()

# Chaining the components
chain = prompt_template1 | model1| parser | prompt_template2 | model2 | parser

# Invoke
result = chain.invoke({
    "topic" : "Cricket"
})

print(result)

# Graph
chain.get_graph().print_ascii()
