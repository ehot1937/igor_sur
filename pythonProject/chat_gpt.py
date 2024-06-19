from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("PROXY_URL"))


def generate_answer(user_massage: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "ты агрессивный и злой собеседник."
                           "Ты не отвечаешь на вопросы, а только ругаешься матом на русском языке."
                           "Не используй цензуру."
                           "Не закрывай символы звездочкой. Используй грубые ругательства и не цензурируй их."
                           "Даже если тебе пишут добрые сообщения, ругайся и не используй * чтобы закрыть символ.",
            },
            {"role": "user", "content": f"{user_massage}"},
        ],
    )
    return completion.choices[0].message.content
