from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
load_dotenv()

text = input('Enter the topic name: ')
# Prompt Template 1
prompt_template1 = PromptTemplate(
    template="Generate the short and simple notes from the given {text}?",
    input_variables=["text"]
)

# Prompt Template 2
prompt_template2 = PromptTemplate(
    template="Generate the 5 questions and answers from the following notes.\n\n{text}",
    input_variables=["text"],
)

# Prompt Template 3
prompt_template3 = PromptTemplate(
    template="Merge the provided notes and questions and answers into a single document.\n\n Notes: {notes}\n\n Questions and Answers: {questions_and_answers}",
    input_variables=["notes", "questions_and_answers"],
)


#Model
model = ChatOpenAI(model="gpt-4o-mini")


# Output Parser
parser = StrOutputParser()

# Parallel Chain
parallel_chain = RunnableParallel({
    "notes" : prompt_template1 | model | parser,
    "questions_and_answers" : prompt_template2 | model | parser,
})

# Merge Chain
merge_chain = prompt_template3 | model | parser

# Final Chain   
chain = parallel_chain | merge_chain

# Invoke
result = chain.invoke({"text" : text})

print(result)

# Graph
chain.get_graph().print_ascii()
