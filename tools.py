from datetime import datetime
from langchain_core.tools import tool

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper


# web search tool using duckduckgo
@tool
def search(query: str) -> str:
    """Search the internet for current information, news, or recent developments.
    
    Args:
        query: The search query string
        
    Returns:
        Search results as text
    """
    try:
        duckduckgo = DuckDuckGoSearchRun()
        result = duckduckgo.run(query)
        return result if result else "No results found."
    except Exception as e:
        return f"Search error: {str(e)}"


# wikipedia lookup tool
@tool
def wikipedia(query: str) -> str:
    """Get encyclopedic information from Wikipedia about topics, history, and facts.
    
    Args:
        query: The topic to look up on Wikipedia
        
    Returns:
        Wikipedia article summary
    """
    try:
        # limit to 500 chars to keep it concise
        wiki_api = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
        result = wiki_api.run(query)
        return result if result else "No Wikipedia article found."
    except Exception as e:
        return f"Wikipedia error: {str(e)}"


# file saving tool
@tool
def save_text_to_file(data: str, filename: str = "research_output.txt") -> str:
    """Save research findings to a text file.
    
    Args:
        data: The text content to save
        filename: Name of the file (default: research_output.txt)
        
    Returns:
        Success or error message
    """
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # add timestamp header to each save
        text = f"\n{'='*60}\n--- Research saved at {timestamp} ---\n{'='*60}\n{data}\n\n"
        
        # append mode so multiple saves don't overwrite
        with open(filename, "a", encoding="utf-8") as f:
            f.write(text)

        return f"✅ Successfully saved research to {filename}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"