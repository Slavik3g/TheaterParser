import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(message, chat_id, token):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        "chat_id": int(chat_id),
        "text": message
    }
    headers = {'Content-Type': 'application/json', }
    response = requests.post(url=url, data=json.dumps(payload), headers=headers)
    return response.json()

message = "Я жив и всё ещё слежу за билетами!"
send_message(message=message, chat_id=CHAT_ID, token=TOKEN)