import json
from .web_search import web_search

def search_hotels(city: str, preferences: str = "best rated") -> str:
    """
    Finds real-time hotel information for a given city by using a specialized web search.
    """
    # Create a specialized, high-quality search query
    query = f"{preferences} hotels in {city}"
    
    try:
        # Re-use the web_search logic
        search_results_json = web_search(query)
        return search_results_json

    except Exception as e:
        return json.dumps({"error": f"Failed to search for hotels: {str(e)}"})
