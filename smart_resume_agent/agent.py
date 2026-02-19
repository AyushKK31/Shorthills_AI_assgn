from google.adk.agents import Agent
from google.adk.models import Gemini

from smart_resume_agent.sub_agents.resume_agent import resume_agent
from smart_resume_agent.sub_agents.job_agent import job_agent
from smart_resume_agent.sub_agents.improvement_agent import improvement_agent

model = Gemini(model="gemini-2.5-flash")

root_agent = Agent(
    name="SmartResumeAnalyzer",
    model=model,
    description="Orchestrates resume analysis workflow.",
    instruction="""
You are the root orchestrator.

1. Ask for resume PDF path.
2. Send it to ResumeAgent.
3. Ask for job role.
4. Send role to JobResearchAgent.
5. Send results to ImprovementAgent.
6. Return final report.
""",
    sub_agents=[resume_agent, job_agent, improvement_agent],
)
