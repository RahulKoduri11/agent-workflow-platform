from agents.llm import ask_llm

def researcher_agent(topic):
    prompt = f"""
    Provide research notes about the following topic.

    Topic:
    {topic}

    Include:
    - Key concepts
    - Technologies
    - Best practices
    - Common challenges

    Return concise bullet points.
    """

    return ask_llm(prompt)