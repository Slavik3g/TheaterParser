from settings import *
from telegram_bot.bot import TelegramBot

import re
import time
import requests



def check_for_update(*, url: str, phrase: str) -> bool:
    """
    Returns False if phrase exists, that means that the service has not been updated
    """
    req = requests.get(url=url)
    if re.search(phrase, req.text):
        return False
    return True


def main():
    theatre_bot = TelegramBot(TOKEN)
    theatre_bot.send_message(text="Hello!", chat_id=CHAT_ID)
    checking_page_url = "https://www.rustheatre.by/?month=6"
    daily_notification = 24
    while True:
        status = check_for_update(url=checking_page_url, phrase="К сожалению, здесь мероприятий нет")
        if status:
            for _ in range(5):
                message = f"Появились билеты в театр!\nСрочно покупайте: {checking_page_url}"
                theatre_bot.send_message(text=message, chat_id=CHAT_ID)
        else:
            daily_notification -= 0.5
            if not daily_notification:
                message = "Я жив и всё ещё слежу за билетами!"
                theatre_bot.send_message(text=message, chat_id=CHAT_ID, disable_notification=True)
                daily_notification = 24
            logger.info(f"I'm alive {daily_notification=}, {status=}")
        time.sleep(1800)


if __name__ == "__main__":
    logger.info('Service has started')
    main()
