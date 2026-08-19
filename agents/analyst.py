from agents.llm import ask_llm

def analyst_agent(plan, research):
    prompt = f"""
    You are a senior software architect.

    PLAN:
    {plan}

    RESEARCH:
    {research}

    Analyze the information and provide:

    1. Recommended architecture
    2. Recommended tech stack
    3. Major risks
    4. Development priorities

    Format your answer clearly.
    """

    return ask_llm(prompt)