from tools import search_weather, search_attractions

def local_guide(state):
    """
    Local Guide: Provides weather and attraction tips.
    """
    dest = state.get("destination")
    if not dest:
        return {"messages": [{"role": "assistant", "content": "Local Guide: Please tell me your destination first!"}]}

    print(f"\n[AGENT] Local Guide is checking weather for {dest}...")
    weather = search_weather(dest)
    
    print(f"[AGENT] Local Guide is looking for attractions in {dest}...")
    attractions = search_attractions(dest)

    response_text = f"Local Guide here! Tips for your trip to {dest}:\n\n"
    response_text += f"Weather Forecast: {weather}\n\n"
    response_text += f"Must-see Attractions: {attractions}"

    return {
        "messages": [{"role": "assistant", "content": response_text}]
    }
