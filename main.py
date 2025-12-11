from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

load_dotenv()

# llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm = ChatGroq(model="llama-3.3-70b-versatile")

response = llm.invoke("what is the meaning of life?")
print(response.content)