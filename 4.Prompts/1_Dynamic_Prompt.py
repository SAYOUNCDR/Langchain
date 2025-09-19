# There are two types of prompts: static and dynamic.
# Static prompts are fixed and do not change based on user input or context.
# Dynamic prompts, on the other hand, can change based on user input, context, or other factors.

# Dynamic prompt example: Uses templates to create prompts that adapt to user input.

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

st.header("Dynamic Prompt Example")
user_input = st.text_input("Enter your name", "John")

# Define a dynamic prompt template
template = "Write a poem about {topic}."

prompt = PromptTemplate(template=template, input_variables=["topic"])
dynamic_prompt = prompt.format(topic=user_input)

if st.button("Generate Poem"):
    result = model.invoke(dynamic_prompt)
    st.write(result.content)
