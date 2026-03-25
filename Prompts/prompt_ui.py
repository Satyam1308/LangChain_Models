from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

#Loading the prompt template
template = load_prompt("template.json")

#Initializing the model
model = ChatOpenAI(model="gpt-4o-mini")

#UI for the prompt
st.header("Reasearch Tool")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


#Invoking the chain
if st.button("Summarize"):
    chain = template | model
    with st.spinner("Summarizing..."):
        response = chain.invoke({
            "paper_input": paper_input, 
            "explanation_style": style_input, 
            "explanation_length": length_input
            })

    #Displaying the response
    st.write(response.content)