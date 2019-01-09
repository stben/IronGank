from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    room_id = models.CharField(max_length=40, primary_key=True)
    room_title = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    room_description = models.CharField(max_length=100)
    is_need_whiteboard = models.BooleanField()
    is_need_code_editor = models.BooleanField()
    is_need_password = models.BooleanField()


class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=100, primary_key=True)


class TimeTable(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE,)
    class_week = models.IntegerField()
    class_day = models.IntegerField()
    class_class = models.IntegerField()


class RoomAndTeacher(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    status = models.BooleanField()

class RoomAndStudent(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE,)
    username = models.ForeignKey(User, on_delete=models.CASCADE,)


class ListOfForbiddenStudents(models.Model):
    room_id = models.ForeignKey('Room', on_delete=models.CASCADE,)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
