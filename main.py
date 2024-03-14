import re
import os
import json
import time
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def check_for_update(url, phrase):
    req = requests.get(url=url)
    if re.search(phrase, req.text):
        return False
    return True


def send_message(message, chat_id, token):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        "chat_id": int(chat_id),
        "text": message
    }
    headers = {'Content-Type': 'application/json', }
    response = requests.post(url=url, data=json.dumps(payload), headers=headers)
    return response.json()


def main():
    hours_to_info = 24.5
    while True:
        status = check_for_update(url="https://www.rustheatre.by/?month=6", phrase="К сожалению, здесь мероприятий нет")
        if status:
            for _ in range(5):
                message = "Появились билеты в театр!\nСрочно покупайте: https://www.rustheatre.by/?month=6"
                send_message(message=message, chat_id=CHAT_ID, token=TOKEN)
        else:
            hours_to_info -= 0.5
            if not hours_to_info:
                message = "Я жив и всё ещё слежу за билетами!"
                send_message(message=message, chat_id=CHAT_ID, token=TOKEN)
                hours_to_info = 24
        time.sleep(1800)


if __name__ == "__main__":
    main()
