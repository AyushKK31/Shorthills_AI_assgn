from google.adk.agents import Agent
from google.adk.models import Gemini
from google.adk.tools.google_search_agent_tool import GoogleSearchAgentTool
from google.adk.tools.google_search_agent_tool import create_google_search_agent
from smart_resume_agent.tools.keyword_tool import extract_keywords

model = Gemini(model="gemini-2.5-flash")

# Workaround: ADK's built-in `google_search` model tool cannot reliably be
# combined with function-calling tools in the same agent request.
# Wrap it in a dedicated sub-agent so this agent can use it alongside
# other tools like `extract_keywords`.
google_search_agent = create_google_search_agent(model)
google_search_tool = GoogleSearchAgentTool(google_search_agent)

job_agent = Agent(
    name="JobResearchAgent",
    model=model,
    description="Research job description and extract keywords.",
    instruction="""
You are a job research agent.
Use google_search_agent to find job descriptions.
Then use extract_keywords tool to extract important skills.
""",
    tools=[google_search_tool, extract_keywords],
)
