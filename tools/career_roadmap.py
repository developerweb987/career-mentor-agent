import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

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

async def get_career_roadmap(career_name: str):
    prompt = f"List the key skills required to become a successful {career_name}. Provide them as a comma-separated list."
    response = await model.run(messages=[{"role": "user", "content": prompt}])
    skills_text = response.output_text.strip()
    skills_list = [skill.strip() for skill in skills_text.split(",") if skill.strip()]
    return skills_list
