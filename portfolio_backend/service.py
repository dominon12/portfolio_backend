from django.conf import settings

import requests 



def build_absolute_uri(request, relative_url):
    uri = request.build_absolute_uri(relative_url)
    return uri.replace('http', 'https')
    # return uri


def send_telegram_bot_message(message: str) -> bool:
    r = requests.get(
        f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={settings.TELEGRAM_ADMIN_CHAT_ID}&parse_mode=HTML&text={message}"
    )
    return r.ok


