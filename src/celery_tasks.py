from celery import Celery
from src.mail import mail, create_message
from asgiref.sync import async_to_sync
from src.config import Config


c_app = Celery()
c_app.conf.broker_url = Config.REDIS_URL
c_app.conf.result_backend = Config.REDIS_URL


@c_app.task()
def send_email(recipients: list[str], subject: str, body: str):

    message = create_message(recipients=recipients, subject=subject, body=body)

    async_to_sync(mail.send_message)(message)
    print("Email sent")
