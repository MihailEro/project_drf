from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_email(course, email):
    send_mail(
        subject='Обновление курса',
        message=f"Обновление курса {course}",
        recipient_list=email,
        from_email=settings.EMAIL_HOST_USER
    )
