from langchain_community.tools import wikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import wikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information"
)