from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.analyst import analyst_agent
from agents.reporter import reporter_agent

task = "Build a personal finance tracking application"

plan = planner_agent(task)
research = researcher_agent(task)
analysis = analyst_agent(plan, research)
report = reporter_agent(plan, research, analysis)

print("=== FINAL REPORT ===")
print(report)