from tools import search_flights, search_hotels

def booking_agent(state):
    """
    Booking Specialist: Finds flights and hotels based on destination and dates.
    """
    dest = state.get("destination")
    dates = state.get("dates")
    budget = state.get("budget", "standard")

    if not dest or not dates:
        return {"messages": [{"role": "assistant", "content": "Flight Specialist: I need destination and dates to book flights!"}]}

    print(f"\n[AGENT] Booking Specialist is searching for flights to {dest}...")
    flight_info = search_flights("Home", dest, dates)
    
    print(f"[AGENT] Booking Specialist is searching for hotels in {dest}...")
    hotel_info = search_hotels(dest, f"{budget} rated")

    response_text = f"Flight Specialist here! I've looked into your trip to {dest} on {dates}:\n\n"
    response_text += f"Flights: {flight_info}\n\n"
    response_text += f"Hotels: {hotel_info}"

    return {
        "messages": [{"role": "assistant", "content": response_text}],
        "flight_options": [flight_info],
        "hotel_options": [hotel_info]
    }
