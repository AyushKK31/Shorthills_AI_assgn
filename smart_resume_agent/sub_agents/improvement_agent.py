from google.adk.agents import Agent
from google.adk.models import Gemini
from smart_resume_agent.tools.report_tool import generate_markdown_report

model = Gemini(model="gemini-2.5-flash")

improvement_agent = Agent(
    name="ImprovementAgent",
    model=model,
    description="Suggests improvements and generates markdown report.",
    instruction="""
You are a resume improvement expert.
Compare resume content with job keywords.
Provide improvement suggestions.
Use generate_markdown_report to format output.
""",
    tools=[generate_markdown_report],
)
