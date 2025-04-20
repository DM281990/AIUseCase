from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")


agent=Agent(
    model=OpenAIChat("gpt-3.5-turbo"),
    description="You are an assistant please reply based ont he question",
    tools=[DuckDuckGoTools()],
    markdown=True
)

agent.print_response("Tell me brief about Diwakar Mishra of Philips")