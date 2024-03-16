from enum import Enum


class LinksEnum(str, Enum):
    send_message_url = 'https://api.telegram.org/bot{bot_token}/sendMessage'
