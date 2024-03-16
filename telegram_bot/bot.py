from .links import LinksEnum

import json
from typing import Optional, Union
import requests


class TelegramBot:
    headers = {'Content-Type': 'application/json', }

    def __init__(self, bot_token):
        self.bot_token = bot_token

    def send_message(self,
                     *,
                     chat_id: Union[int, str],
                     text: str,
                     message_thread_id: Optional[int] = None,
                     parse_mode: Optional[str] = "",
                     entities: Optional[list] = None,
                     disable_notification: Optional[bool] = False,
                     protect_content: Optional[bool] = False,
                     ) -> json:
        url = LinksEnum.send_message_url.format(bot_token=self.bot_token)
        payload = {
            "chat_id": chat_id,
            "text": text,
            "message_thread_id": message_thread_id,
            "parse_mode": parse_mode,
            "entities": entities,
            "disable_notification": disable_notification,
            "protect_content": protect_content
        }
        response = requests.post(url=url, data=json.dumps(payload), headers=self.headers)
        return response.json()
