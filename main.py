from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from tools import search_tool



load_dotenv()

# llm = ChatOpenAI(model="gpt-4o-mini")
# llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
llm = ChatGroq(model="llama-3.3-70b-versatile")

# response = llm.invoke("what is the meaning of life?")
# print(response.content)

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
        "system",
            """
            You are a research assistant that will help generate a research paper.
            
            You may ONLY use the tools provided in the 'tools' list.
            DO NOT create or refer to any tool name that is not explicitly provided.
            The only tool you have is: "search".

            Wrap the output in the required Pydantic format:
            {format_instructions}
            """
        ),

        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool]

agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools= tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What can i help you Research? ")

raw_response = agent_executor.invoke({"query": query})
# print(raw_response)

structured_response = parser.parse(raw_response.get("output"))
#print(structured_response) 
#print(structured_response.topic) 

try: 
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)

