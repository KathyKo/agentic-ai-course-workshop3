import json
from .web_search import web_search

def search_attractions(city: str, interest: str = "top attractions") -> str:
    """
    Finds top attractions and things to do in a given city.
    """
    query = f"{interest} in {city} tourist spots"
    
    try:
        search_results_json = web_search(query)
        return search_results_json

    except Exception as e:
        return json.dumps({"error": f"Failed to search for attractions: {str(e)}"})
