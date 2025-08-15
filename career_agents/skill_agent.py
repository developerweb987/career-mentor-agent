from agents import Agent
from tools.career_roadmap import get_career_roadmap

skill_agent = Agent(
    name="SkillAgent",
    instructions="Given a career choice, list the essential skills needed for that career.",
    model=None,
    handoffs=[]
)
