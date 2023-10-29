from django.db import models

from course.models import Course
from lessons.models import Lesson
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Payment(models.Model):

    METHOD_CHOICES = [('card', 'перевод'), ('cash', 'наличные'), ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    pay_date = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    pay_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    pay_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    pay_summ = models.IntegerField(verbose_name='сумма оплаты')
    pay_method = models.CharField(choices=METHOD_CHOICES, default=METHOD_CHOICES[1], verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.pay_summ}'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплаты'
