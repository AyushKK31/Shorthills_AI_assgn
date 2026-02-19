def generate_markdown_report(suggestions: str) -> str:
    """
    Generate a markdown formatted report.
    """
    report = f"""
# Resume Improvement Report

## Suggestions:
{suggestions}

---

Generated using Smart Resume Analyzer (Google ADK Multi-Agent System)
"""
    return report
