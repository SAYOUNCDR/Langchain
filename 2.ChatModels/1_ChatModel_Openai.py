from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temprature defines the output randomness
# Lower values means more predictable
# Higher values means more random and creative
# factual (maths, code, facts) - 0.0 - 0.3
# Balanced response (general QA, explanation) - 0.5 - 0.7
# Creative writing or Story telling - 0.9 - 1.2
# Maximum randomness (wild ideas, brainstorming) - 1.5+
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5, max_completion_tokens=10)
result = model.invoke("Write a poem")

# it will return different result {key:values} i.e tockens , etc than the llm
# print(result)
print(result.content)  # Now this will give only the response i.e ans
