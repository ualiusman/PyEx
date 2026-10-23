import os

from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError(
        "DEEPSEEK_API_KEY is missing. "
        "Add it to your .env file."
    )

llm = LLM(
    model="deepseek/deepseek-chat",
    base_url="https://api.deepseek.com",
    api_key=api_key,
    temperature=0.2,
    timeout=120,
    max_tokens=3000,
)