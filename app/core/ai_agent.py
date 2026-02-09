from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

from langchain_core.messages.ai import AIMessage

from app.config.settings import settings


def get_response_from_ai_agents(llm_id: str, messages: str, allow_search: bool, system_prompt: str) -> str:

    llm = ChatGroq(api_key=settings.GROQ_API_KEY, model=llm_id)

    tools = [TavilySearchResults(api_key=settings.TAVILY_API_KEY, max_results=2)] if allow_search else []

    agent = create_react_agent(
        model=llm,
        tools=tools,
        )

    state = {"messages": messages}

    response = agent.invoke(state)

    messages = response.get("messages")
    ai_message = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_message[-1] if ai_message else "No response generated."


