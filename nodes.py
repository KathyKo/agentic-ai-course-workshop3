from typing import Literal
from .state import State
from .agents import (
    travel_orchestrator,
    concierge,
    booking_agent,
    local_guide,
    travel_summarizer
)

def human_node(state: State) -> dict:
    """Gets user input and resets state for the next turn."""
    user_input = input("\nYou (Traveler): ").strip()
    return {
        "messages": [{"role": "user", "content": user_input}],
        "is_complete": False
    }

def orchestrator_node(state: State) -> dict:
    """Calls the orchestrator to decide which agent should speak."""
    print("\n[SYSTEM] Orchestrator is analyzing your request...")
    return travel_orchestrator(state)

def concierge_node(state: State) -> dict:
    """Node for the Concierge agent."""
    print("\n[AGENT] Concierge is responding...")
    return concierge(state)

def booking_node(state: State) -> dict:
    """Node for the Booking Specialist agent."""
    return booking_agent(state)

def local_guide_node(state: State) -> dict:
    """Node for the Local Guide agent."""
    return local_guide(state)

def summarizer_node(state: State) -> dict:
    """Node for the Travel Summarizer agent."""
    print("\n[AGENT] Finalizing your itinerary...")
    return travel_summarizer(state)

def orchestrator_routing(state: State) -> Literal["concierge", "booking_agent", "local_guide", "summarizer"]:
    """Determines which specialized agent node to go to next."""
    return state.get("next_agent", "concierge")

def check_exit_condition(state: State) -> Literal["summarizer", "orchestrator"]:
    """Checks if the user wants to exit or if the process should continue."""
    messages = state.get("messages", [])
    if messages:
        last_msg = messages[-1].get("content", "").lower()
        if "exit" in last_msg or "quit" in last_msg or "done" in last_msg:
            return "summarizer"
    return "orchestrator"
