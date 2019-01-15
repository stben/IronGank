from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sid = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return User.objects.get(id=self.user_id).username
