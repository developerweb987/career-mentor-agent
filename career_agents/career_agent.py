from agents import Agent

class CareerAgent(Agent):
    def __init__(self, model):
        super().__init__(
            name="CareerAgent",
            instructions="You suggest career paths based on the student's interests."
        )
