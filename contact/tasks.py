from django.core.mail import EmailMessage

import celery

from portfolio_backend import service


@celery.shared_task
def on_new_contact_request(name, email, comment):
    message = f"<b>New contact request</b>%0A%0A<b>From</b> {name}%0A<b>Email</b> {email}"
    if comment:
        message += f"%0A%0A${comment}"
    service.send_telegram_bot_message(message)


def on_new_order(data):
    message = f'''
        Контактные данные

        Имя: {data["firstName"]}
        Фамилия: {data["lastName"]}
        Телефон: {data["phone"]}

        Адрес

        Откуда: {data["from"]}
        Куда: {data["to"]}
    '''
    email = EmailMessage(
        subject="Новый заказ на вывоз тела", 
        body=message,
        to=["lehmann1967@inbox.ru"]
    )
    email.send()
