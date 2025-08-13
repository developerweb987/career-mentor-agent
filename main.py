import os
import asyncio
from dotenv import load_dotenv
from career_agents.career_agent import CareerAgent
from career_agents.skill_agent import SkillAgent
from career_agents.job_agent import JobAgent
from tools.career_roadmap import get_career_roadmap
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

career_agent = CareerAgent(model)
skill_agent = SkillAgent(model)
job_agent = JobAgent(model)

async def career_mentor_loop():
    agent = Agent(
        name="CareerMentorAgent",
        instructions=(
            "Guide students through career exploration. "
            "Use CareerAgent to suggest fields, "
            "SkillAgent for skill-building plans, "
            "JobAgent to show real-world job roles."
        ),
        tools=[Agent(
            name="CareerRoadmapTool",
            instructions="Provide skill roadmap for a given field",
            model=model
        ).as_tool(
            tool_name="get_career_roadmap",
            tool_description="Give relevant skill set for the required field"
        )],
        handoffs=[skill_agent, job_agent]
    )

    chat_history = []

    print("Welcome to Career Mentor Agent! Start your career exploration.\n")

    while True:
        user_input = input("Your question: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("Exiting Career Mentor. Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            result = await Runner.run(agent, chat_history, run_config=config)
            response = result.final_output
            print(f"\n{response}\n")
            chat_history.append({"role": "developer", "content": response})
        except Exception as e:
            print(f"Error: {str(e)}\n")

if __name__ == "__main__":
    asyncio.run(career_mentor_loop())
