from django.conf import settings

import requests 


def send_telegram_bot_message(message: str) -> int:
    r = requests.get(
        f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={settings.TELEGRAM_ADMIN_CHAT_ID}&parse_mode=HTML&text={message}"
    )
    return r.ok


