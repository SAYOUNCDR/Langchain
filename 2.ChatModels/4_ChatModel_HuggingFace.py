from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Use conversational task
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="conversational",  
    huggingfacehub_api_token=hf_token,
    max_new_tokens=100,
)


model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")

print(result.content)
