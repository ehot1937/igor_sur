from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    flag = True
    while flag:
        massage = input()
        if massage == "stop":
            flag = False
            break

        client = OpenAI(
                        base_url="https://api.proxyapi.ru/openai/v1")

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                {"role": "user", "content": f"{massage}"}
            ],
            max_tokens=50
        )

        print(completion.choices[0].message.content)
