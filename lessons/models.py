from django.db import models
from course.models import Course

from config import settings
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Lesson(models.Model):
    lesson_name = models.CharField(max_length=100, verbose_name="название урока")
    lesson_description = models.TextField(verbose_name="описание урока", **NULLABLE)
    lesson_preview = models.ImageField(
        upload_to="course/", verbose_name="превью", **NULLABLE
    )
    lesson_video_url = models.CharField(
        max_length=255, verbose_name="ссылка на видео", **NULLABLE
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='студент', **NULLABLE)

    def __str__(self):
        return f"{self.lesson_name} {self.lesson_description}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
