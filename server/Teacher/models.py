from django.db import models


class Room(models.Model):
    room_id = models.CharField(max_length=40, primary_key=True)
    room_title = models.CharField(max_length=100)
    college = models.CharFielsd(max_length=100)
    password = models.CharFielsd(max_length=100)
    room_description = models.CharFielsd(max_length=100)
    is_need_whiteboard = models.BooleanField()
    is_need_code_editor = models.BooleanField()
    is_need_password = models.BooleanField()


class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_id = models.CharField(max_length=100, primary_key=True)


class TimeTable(models.Model):
    room_num = models.CharField(max_length=100, foreign_key=True)
    class_week = models.IntegerField(max_length=10)
    class_day = models.IntegerField(max_length=10)
    class_class = models.IntegerField(max_length=10)


class RoomAndTeacher(models.Model):
    room_id = models.CharField(max_length=100, foreign_key=True)
    username = models.CharField(max_length=100, foreign_key=True)
    status = models.BooleanField()
