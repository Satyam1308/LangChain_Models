from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

template_prompt1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ["topic"]
)

template_prompt2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text. /n {text}',
    input_variables = ["text"]
)

parser = StrOutputParser()
chain = template_prompt1 | model | parser | template_prompt2 | model | parser


result = chain.invoke({
    "topic": "AI"
})

print(result)