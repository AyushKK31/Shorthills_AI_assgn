from google.adk.agents import Agent
from google.adk.models import Gemini
from smart_resume_agent.tools.pdf_tool import extract_pdf_text

model = Gemini(model="gemini-2.5-flash")

resume_agent = Agent(
    name="ResumeAgent",
    model=model,
    description="Extracts text from a resume PDF.",
    instruction="""
You are a resume extraction agent.
Your job is to extract text from a given PDF resume file path
using the extract_pdf_text tool.
""",
    tools=[extract_pdf_text],
)
