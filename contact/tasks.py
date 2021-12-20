import celery

from portfolio_backend import service


@celery.shared_task
def on_new_contact_request(name, email, comment):
    message = f"<b>New contact request</b>%0A%0A<b>From</b> {name}%0A<b>Email</b> {email}"
    if comment:
        message += f"%0A%0A${comment}"
    service.send_telegram_bot_message(message)