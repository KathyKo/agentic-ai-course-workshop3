#  Travel Planning Agent (Multi-Agent System)

## Project Overview
This project is an AI-powered multi-agent travel agency designed to help users plan a complete trip. Whether it's finding flights, hotels, or discovering local attractions, our expert agents collaborate to generate a personalized itinerary. 

This system demonstrates a robust **Orchestrator-Worker architecture** using **LangGraph**, where a specialized coordinator manages the flow between different domain experts.

## Key Features
- **Multi-Agent Coordination**: An intelligent Orchestrator routes tasks to specialized agents (Concierge, Booking Specialist, Local Guide).
- **Real-time Tool Integration**: Agents use real APIs (Google Custom Search, OpenWeather) to provide up-to-date travel information.
- **Dynamic State Management**: Shared state maintains user preferences and gathered travel data throughout the session.
- **Smart Itinerary Generation**: A final summary agent compiles all gathered data into a beautiful, ready-to-use travel plan.

## Agent Roles & Personas
1. **Travel Orchestrator (The Coordinator)**: Analyzes the conversation and assigns the most suitable expert to the task.
2. **Travel Concierge (The Facilitator)**: Interacts with the user to gather essential trip details (destination, dates, budget).
3. **Booking Specialist (The Logistician)**: Specialized in finding real-time flight and hotel options based on user constraints.
4. **Local Guide (The Insider)**: Provides weather forecasts and suggests must-see tourist attractions.
5. **Master Planner (The Summarizer)**: Reviews all expert input and creates the final, cohesive itinerary.

## Tools Integrated
- **`search_flights`**: Searches for current flight options using a web search tool.
- **`search_hotels`**: Finds top-rated accommodations based on destination and budget.
- **`search_weather`**: Fetches 2-day weather forecasts via OpenWeather API.
- **`search_attractions`**: Suggests popular landmarks and activities in the target city.
- **`web_search`**: A generic real-time information retrieval tool.

## Setup Instructions

### 1. Prerequisites
Ensure you have Python installed. We recommend using **`uv`** or **`pip`**.

### 2. Environment Configuration
Copy the `.env.example` file and rename it to `.env`:
```sh
cp .env.example .env
```
Fill in the following keys:
- `OPENAI_API_KEY`: Your OpenAI API key.
- `CUSTOM_SEARCH_API_KEY`: Google Custom Search API Key.
- `CUSTOM_SEARCH_CX`: Google Custom Search Engine ID (CX).
- `OPENWEATHER_API_KEY`: OpenWeatherMap API Key.

### 3. Install Dependencies
```sh
pip install langgraph langchain-openai python-dotenv requests
```

### 4. Run the Agents
```sh
python main.py
```

## How to use
- Simply start chatting! (e.g., "I want to plan a trip to Tokyo in December.")
- The agents will ask for more details if needed.
- Type **'exit'** or **'done'** to generate your final itinerary summary.
