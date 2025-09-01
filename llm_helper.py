from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()
llm = ChatGroq(groq_api_key = os.getenv("GROQ_API_KEY"),model_name="openai/gpt-oss-120b")

if __name__ == "__main__":
    respone = llm.invoke("What i sthe capital of India ?")
    print(respone.content)

