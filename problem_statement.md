# Problem Statement: Smart Resume Analyzer using Multi-Agent System

## Objective
Build a multi-agent system using Google ADK that analyzes a user's resume against a job description and suggests improvements.

## Problem
Many candidates apply to jobs without optimizing resumes for specific job descriptions. This reduces their chances of passing ATS screening.

## Solution
This system:
1. Extracts resume text.
2. Searches and analyzes job description using google_search.
3. Compares resume with job keywords.
4. Generates improvement suggestions in markdown format.

## Agents Used
- Root Agent (Orchestrator)
- Resume Extraction Agent
- Job Research Agent
- Resume Improvement Agent

## Tools Used
- Built-in google_search tool
- extract_pdf_text
- extract_keywords
- generate_markdown_report
