import os

from dotenv import load_dotenv
from openai import OpenAI

from scripts.welcome_prompt import build_system_prompt


load_dotenv(override=True)


def get_assistant_reply(messages: list[dict]) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    model = os.getenv("OPENAI_MODEL", "gpt-5.4")

    response = client.chat.completions.create(
        model=model,
        temperature=0.4,
        messages=[{"role": "system", "content": build_system_prompt()}, *messages],
    )

    content = response.choices[0].message.content
    if isinstance(content, str):
        return content.strip()

    raise ValueError("Assistant response was empty or not plain text.")
