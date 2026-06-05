import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq # Change this line

load_dotenv()

# Use Groq instead of ChatOpenAI
llm = ChatGroq(
    model="llama-3.3-70b-versatile", # Groq's high-speed model
    api_key=os.getenv("GROQ_API_KEY")
)

with open("bad_code.py", "r") as file:
    code_to_review = file.read()

prompt = f"""
You are a Senior DevOps and Software Engineer. 
Review the following code for bugs, security issues, and performance improvements.
CODE TO REVIEW:
{code_to_review}
"""

response = llm.invoke(prompt)

print("--- AI REVIEW RESULTS ---")
print(response.content)