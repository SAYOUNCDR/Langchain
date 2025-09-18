from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents = [
    "LangChain is a framework for developing applications powered by language models.",
    "It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.",
    "LangChain is modular and can be easily customized.",
    "Testing document embeddings with LangChain.",
]
result = embeddings.embed_documents(documents)

print(str(result))
