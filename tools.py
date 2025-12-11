from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()

def search_func(query: str):
    """Search the web using DuckDuckGo."""
    return search.run(query)

search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information"
)