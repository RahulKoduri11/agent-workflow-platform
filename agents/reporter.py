from agents.llm import ask_llm

def reporter_agent(plan, research, analysis):
    prompt = f"""
    Create a professional project report.

    PLAN:
    {plan}

    RESEARCH:
    {research}

    ANALYSIS:
    {analysis}

    Generate a report with:

    1. Executive Summary
    2. Project Objectives
    3. Recommended Architecture
    4. Recommended Tech Stack
    5. Risks
    6. Development Roadmap
    7. Final Recommendation
    """

    return ask_llm(prompt)