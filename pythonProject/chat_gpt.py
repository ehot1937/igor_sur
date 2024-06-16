from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(base_url="https://api.proxyapi.ru/openai/v1")


def generate_answer(user_massage: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "you are an aggressive and angry interlocutor who does not respond to user messages, but swears in Russian in response to him",
            },
            {"role": "user", "content": f"{user_massage}"},
        ],
    )
    return completion.choices[0].message.content
