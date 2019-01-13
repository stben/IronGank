from django.db import models
from django.contrib.auth.models import User
from student.models import Student


class College(models.Model):
    name = models.CharField('院系名', max_length=100, unique=True)
    college_id = models.CharField('院系号', max_length=100, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "院系信息"
        verbose_name_plural = "院系信息"


class Room(models.Model):
    name = models.CharField('房间名', max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE, verbose_name='所属院系')
    password = models.CharField('房间密码', max_length=16, null=True, blank=True)
    description = models.CharField('房间描述', max_length=1000)
    is_need_whiteboard = models.BooleanField('是否有白板')
    is_need_code_editor = models.BooleanField('是否有代码编辑器')
    is_need_password = models.BooleanField('是否设置密码')

    class Meta:
        verbose_name = "房间信息"
        verbose_name_plural = "房间信息"


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
