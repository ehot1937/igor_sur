import os
import telebot
from pythonProject.chat_gpt import generate_answer
from pythonProject.delete_webhook import delete_webhook


API_TOKEN = os.getenv("TELEBOT_TOKEN")
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Ну привет, петушок")


@bot.message_handler()
def echo_message(message):
    response = generate_answer(user_massage=message.text)
    bot.reply_to(message, response)
    print(f"Сообщение: [{message.text}] от пользователя {message.from_user.username}")


if __name__ == "__main__":
    delete_webhook()
    bot.polling(none_stop=True)
