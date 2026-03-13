from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def travel_orchestrator(state):
    """
    Analyzes the travel planning progress and selects the next specialized agent.
    """
    messages = state.get("messages", [])
    destination = state.get("destination")
    dates = state.get("dates")
    budget = state.get("budget")
    
    # Extract conversation for LLM context
    conversation_text = ""
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        conversation_text += f"{role}: {content}\n"

    system_prompt = f"""You are the Head Travel Coordinator. Your job is to select the best expert agent to help the customer based on their current progress.

Current Progress:
- Destination: {destination if destination else 'Not set'}
- Dates: {dates if dates else 'Not set'}
- Budget: {budget if budget else 'Not set'}

Available Expert Agents:
1. concierge: Use this if we are still missing basic info (Destination, Dates, or Budget) or if the user just wants to chat.
2. booking_agent: Use this once we have Destination and Dates to search for flights and hotels.
3. local_guide: Use this to provide weather info and suggest attractions once the destination is known.
4. summarizer: Use this ONLY when the travel plan is complete and you want to present the final itinerary to the user.

Respond with ONLY the name of the agent (concierge, booking_agent, local_guide, or summarizer).
"""

    user_prompt = f"Conversation History:\n{conversation_text}\n\nWho should speak next?"

    try:
        llm = ChatOpenAI(model="gpt-5-mini-2025-08-07", temperature=0)
        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])
        selected_agent = str(response.content).strip().lower()
        
        # Validation
        valid_agents = ["concierge", "booking_agent", "local_guide", "summarizer"]
        if selected_agent not in valid_agents:
            selected_agent = "concierge"
            
        return {"next_agent": selected_agent}
    except Exception as e:
        print(f"Orchestrator error: {e}")
        return {"next_agent": "concierge"}
