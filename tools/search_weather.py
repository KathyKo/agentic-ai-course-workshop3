import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def search_weather(city: str) -> str:
    """
    Gets the 2-day weather forecast for a specific city.
    """
    if not OPENWEATHER_API_KEY:
        return json.dumps({"error": "OpenWeather API key not configured."})

    api_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "cnt": 16 
    }
    
    try:
        response = requests.get(api_url, params=params, timeout=5)
        response.raise_for_status()
        forecast_data = response.json()
        
        list_data = forecast_data.get("list", [])
        
        if not list_data:
            return json.dumps({"error": f"No forecast data found for city '{city}'."})

        # Tomorrow and the day after (roughly)
        day1_forecast = list_data[7] 
        day2_forecast = list_data[15]

        simplified_forecasts = [
            {
                "day": "Tomorrow",
                "summary": day1_forecast.get("weather", [{}])[0].get("description"),
                "temp": day1_forecast.get("main", {}).get("temp"),
            },
            {
                "day": "The Day After Tomorrow",
                "summary": day2_forecast.get("weather", [{}])[0].get("description"),
                "temp": day2_forecast.get("main", {}).get("temp"),
            }
        ]
            
        return json.dumps(simplified_forecasts)

    except requests.exceptions.RequestException as e:
        return json.dumps({"error": f"Error connecting to Forecast API: {str(e)}"})
    except Exception as e:
        return json.dumps({"error": f"An unexpected error occurred: {str(e)}"})
