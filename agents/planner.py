from agents.llm import ask_llm

def planner_agent(task):
    prompt = f"""
    Break the following task into numbered steps.

    Task:
    {task}

    Return only the steps.
    """

    return ask_llm(prompt)