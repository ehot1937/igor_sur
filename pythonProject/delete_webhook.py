import os
import requests

API_TOKEN = os.getenv("TELEBOT_TOKEN")


def delete_webhook():
    url = f"https://api.telegram.org/bot{API_TOKEN}/deleteWebhook"

    response = requests.get(url)
    if response.status_code == 200:
        print("Webhook deleted successfully")
    else:
        print("Failed to delete webhook")
