from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

def travel_summarizer(state):
    """
    Summarizes all the gathered information into a final itinerary.
    """
    dest = state.get("destination")
    dates = state.get("dates")
    budget = state.get("budget")
    messages = state.get("messages", [])

    conversation_text = ""
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        conversation_text += f"{role}: {content}\n"

    system_prompt = """You are a Master Travel Planner. 
    Review the conversation and all the gathered information (flights, hotels, weather, attractions).
    Create a beautiful, organized final travel itinerary for the user.
    The itinerary should be concise but cover everything discussed.
    Include a warm closing message."""

    user_prompt = f"Trip Details:\nDestination: {dest}\nDates: {dates}\nBudget: {budget}\n\nFull Conversation:\n{conversation_text}"

    try:
        llm = ChatOpenAI(model="gpt-5-mini-2025-08-07", temperature=0.7)
        response = llm.invoke([
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt)
        ])
        
        summary = str(response.content)
        print("\n=== FINAL TRAVEL ITINERARY ===\n")
        print(summary)
        print("\n==============================\n")
        
        return {
            "messages": [{"role": "assistant", "content": summary}],
            "is_complete": True
        }
    except Exception as e:
        print(f"Summarizer error: {e}")
        return {"is_complete": True}
