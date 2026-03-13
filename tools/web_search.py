import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

CUSTOM_SEARCH_API_KEY = os.getenv("CUSTOM_SEARCH_API_KEY")
CUSTOM_SEARCH_CX = os.getenv("CUSTOM_SEARCH_CX")

def web_search(query: str) -> str:
    """
    Searches the web for real-time information using Google Custom Search.
    """
    if not CUSTOM_SEARCH_API_KEY or not CUSTOM_SEARCH_CX:
        return json.dumps({"error": "Google Search API keys not configured."})

    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": CUSTOM_SEARCH_API_KEY,
        "cx": CUSTOM_SEARCH_CX,
        "q": query,
        "num": 3 
    }
    
    try:
        response = requests.get(search_url, params=params, timeout=5)
        response.raise_for_status()
        search_data = response.json()
        
        results = search_data.get("items", [])
        
        if not results:
            return json.dumps({"error": f"No web search results found for query: '{query}'"})
            
        simplified_results = []
        for item in results:
            simplified_results.append({
                "title": item.get("title"),
                "snippet": item.get("snippet"),
                "source": item.get("link")
            })
            
        return json.dumps(simplified_results)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"Error connecting to Google Search API: {str(e)}"})
