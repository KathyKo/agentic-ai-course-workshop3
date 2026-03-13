import json
from .web_search import web_search

def search_flights(origin_city: str, destination_city: str, travel_date: str) -> str:
    """
    Finds potential flight options using a specialized web search.
    'travel_date' should be in YYYY-MM-DD format.
    """
    # Create a specialized search query
    query = (
        f"flights from {origin_city} to {destination_city} "
        f"on {travel_date}"
    )
    
    try:
        # Use web_search internally
        search_results_json = web_search(query)
        return search_results_json

    except Exception as e:
        return json.dumps({"error": f"Failed to search for flights: {str(e)}"})
