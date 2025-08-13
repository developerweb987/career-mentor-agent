from agents import Agent

class JobAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="JobAgent",
            instructions="You provide real-world job roles based on the skills of the student."
        )
