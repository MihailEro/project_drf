from django.core.mail import send_mail
from django.conf import settings

from course.models import Course, Subscribe


def send_mail_for_update(course_id):
    course = Course.objects.get(pk=course_id)
    subscribes = Subscribe.objects.filter(course=course_id)
    for subscribe in subscribes:
        send_mail(
            subject=f'Обновление в {course.course_name}.',
            message=f'Курс {course.course_name} был обновлен.',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscribe.user.email]
            )
