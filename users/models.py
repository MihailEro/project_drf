from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="электронная почта")
    phone = models.CharField(max_length=50, verbose_name="телефон", **NULLABLE)
    city = models.CharField(max_length=20, verbose_name="город", **NULLABLE)
    avatar = models.ImageField(upload_to="users/", verbose_name="аватар", **NULLABLE)

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
