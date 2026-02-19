from google.adk.agents import Agent
from google.adk.models import Gemini
from tools.report_tool import generate_markdown_report

model = Gemini(model="gemini-1.5-flash")

improvement_agent = Agent(
    name="ImprovementAgent",
    model=model,
    description="Suggests improvements and generates markdown report.",
    instructions="""
    You are a resume improvement expert.
    Compare resume content with job keywords.
    Provide clear improvement suggestions.
    Use generate_markdown_report tool to format the output.
    """,
    tools=[generate_markdown_report],
)
