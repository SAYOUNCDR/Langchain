import os

os.environ["HF_HOME"] = "E:/huggingface_cache"

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Single text
text= "This is a test sentence"
vector = embedding.embed_query(text)
print(str(vector))

# List of texts or documents
texts = ["This is a test sentence", "This is another test sentence"]
vectors = embedding.embed_documents(texts)
print(str(vectors))