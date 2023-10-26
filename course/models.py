from django.db import models

from config import settings
from users.models import User


NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    course_name = models.CharField(max_length=100, verbose_name="название курса")
    course_preview = models.ImageField(
        upload_to="course/", verbose_name="превью", **NULLABLE
    )
    course_description = models.TextField(verbose_name="описание", **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='студенты', **NULLABLE)

    def __str__(self):
        return f"{self.course_name} {self.course_description}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Subscribe(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.course}:{self.user}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
