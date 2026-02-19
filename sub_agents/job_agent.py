from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools import google_search
from tools.keyword_tool import extract_keywords

model = Gemini(model="gemini-1.5-flash")

job_agent = Agent(
    name="JobResearchAgent",
    model=model,
    description="Research job description and extract keywords.",
    instructions="""
    You are a job research agent.
    Use google_search to find relevant job description details.
    Then use extract_keywords tool to extract important skills and keywords.
    """,
    tools=[google_search, extract_keywords],
)
