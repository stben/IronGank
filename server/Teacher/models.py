from django.db import models
from django.contrib.auth.models import User
from Student.models import Student


class College(models.Model):
    name = models.CharField('院系名',max_length=100)
    college_id = models.CharField('院系号',max_length=100)
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
    class_class = models.IntegerField()
    description = models.CharField(max_length=1000)


class RoomAndTeacher(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()


class RoomAndStudent(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField()


class ListOfForbiddenStudents(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
