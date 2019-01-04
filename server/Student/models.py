from django.db import models
from django.contrib.auth.models import AbstractUser


# 用户类，老师的用户名用email 学生的用手机号
class User(AbstractUser):
    sid = models.CharField(max_length=20, blank=True)

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']
