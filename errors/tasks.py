import celery

from portfolio_backend import service


@celery.shared_task
def on_new_error_feedback(comment: str):
    message = f"<b>New error feedback</b>%0A%0A{comment}"
    service.send_telegram_bot_message(message)


@celery.shared_task
def on_new_client_error(
    name: str, 
    message: str, 
    url: str,
    user_agent: str,
    ip_address: str
):
    message = f"<b>{name}: {message}</b>%0A%0A{url}%0A%0A{user_agent}%0A%0A{ip_address}"
    service.send_telegram_bot_message(message)