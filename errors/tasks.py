import celery

from portfolio_backend import service


@celery.shared_task
def on_new_error_feedback(comment: str):
    message = f"<b>New error feedback</b>%0A%0A{comment}"
    service.send_telegram_bot_message(message)