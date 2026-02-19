from google.adk.agents import Agent
from google.adk.models import Gemini

from sub_agents.resume_agent import resume_agent
from sub_agents.job_agent import job_agent
from sub_agents.improvement_agent import improvement_agent

model = Gemini(model="gemini-1.5-flash")

root_agent = Agent(
    name="SmartResumeAnalyzer",
    model=model,
    description="Orchestrates resume analysis workflow.",
    instructions="""
    You are the root orchestrator agent.

    Workflow:
    1. Ask user for resume PDF file path.
    2. Send file path to ResumeAgent to extract text.
    3. Ask user for job role.
    4. Send job role to JobResearchAgent to research and extract keywords.
    5. Send resume text + job keywords to ImprovementAgent.
    6. Return final formatted report to user.
    """,
    sub_agents=[resume_agent, job_agent, improvement_agent],
)
