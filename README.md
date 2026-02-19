# Smart Resume Analyzer - Multi-Agent System (Google ADK)

## Description
This project implements a multi-agent system using Google ADK to analyze resumes against job descriptions and suggest improvements.

## Setup

1. Create virtual environment
2. Install requirements:
   pip install -r requirements.txt
3. Add your Gemini API key in .env:
   GOOGLE_API_KEY=your_key_here

## Run

CLI Mode:
adk run resume_agent

Web Mode:
adk web

## Architecture
- Root Agent (Orchestrator)
- Resume Extraction Agent
- Job Research Agent
- Resume Improvement Agent

## Tools
- google_search (built-in)
- extract_pdf_text
- extract_keywords
- generate_markdown_report
