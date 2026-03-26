from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()
parser = JsonOutputParser()

template_prompt = PromptTemplate(
    template = 'Write a 5 line summary on {topic}. /n {formatted_message}',
    input_variables = ["topic"],
    partial_variables = {
        "formatted_message": parser.get_format_instructions()
    }
)

chain = template_prompt | model | parser

result = chain.invoke({
    "topic": "ML"
})

print(result)