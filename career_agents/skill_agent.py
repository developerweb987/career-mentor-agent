from agents import Agent

class SkillAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="SkillAgent",
            instructions="You provide skill-building plans for a given career field."
        )
