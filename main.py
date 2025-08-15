import os
import asyncio
from dotenv import load_dotenv

from career_agents.career_agent import career_agent
from career_agents.skill_agent import skill_agent
from career_agents.job_agent import job_agent

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in .env")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
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

career_agent.model = model
skill_agent.model = model
job_agent.model = model

career_agent.handoffs = [skill_agent]
skill_agent.handoffs = [job_agent]

async def career_mentor_loop():
    mentor_agent = Agent(
        name="CareerMentorAgent",
        instructions=(
            "Guide students through career exploration. "
            "Use CareerAgent to suggest fields, "
            "SkillAgent for skill-building plans, "
            "JobAgent to show real-world job roles."
        ),
        model=model,
        handoffs=[career_agent, skill_agent, job_agent]
    )

    chat_history = []

    print("\n Welcome to Career Mentor Agent! Start your career exploration.\n")

    while True:
        user_input = input("Your question: ").strip()
        if user_input.lower() in ["quit", "exit"]:
            print("\n Exiting Career Mentor. Goodbye!")
            break

        chat_history.append({"role": "user", "content": user_input})

        try:
            result = await Runner.run(mentor_agent, chat_history, run_config=config)
            response = result.final_output
            print(f"\n {response}\n")
            chat_history.append({"role": "assistant", "content": response})
        except Exception as e:
            print(f"\n Error: {str(e)}\n")

if __name__ == "__main__":
    asyncio.run(career_mentor_loop())
