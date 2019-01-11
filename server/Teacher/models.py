from django.db import models
from django.contrib.auth.models import User
from Student.models import Student


class College(models.Model):
    name = models.CharField('院系名', max_length=100, unique=True)
    college_id = models.CharField('院系号', max_length=100, unique=True)

    class Meta:
        verbose_name = "院系信息"
        verbose_name_plural = "院系信息"


class Room(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    password = models.CharField(max_length=16)
    description = models.CharField(max_length=1000)
    is_need_whiteboard = models.BooleanField()
    is_need_code_editor = models.BooleanField()
    is_need_password = models.BooleanField()


class TimeTable(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    class_week = models.IntegerField()
    class_day = models.IntegerField()
    begin = models.CharField(max_length=100, default="10:00")
    end = models.CharField(max_length=100, default="11:00")
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default = False)


class RoomAndTeacher(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()


class RoomAndStudent(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.IntegerField()
    # 0 表示已通过，1 表示申请中， 2表示已移除


class ListOfForbiddenStudents(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
