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
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE,
        verbose_name='所属院系')
    password = models.CharField('房间密码',
                                max_length=16,
                                null=True,
                                blank=True)
    description = models.CharField('房间描述', max_length=1000)
    is_need_whiteboard = models.BooleanField('是否有白板')
    is_need_code_editor = models.BooleanField('是否有代码编辑器')
    is_need_password = models.BooleanField('是否设置密码')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "房间信息"
        verbose_name_plural = "房间信息"


class TimeTable(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name='房间名')
    class_week = models.IntegerField('周数')
    class_day = models.IntegerField('工作日')
    begin = models.CharField('起始时间',
                             max_length=100,
                             default="10:00")
    end = models.CharField('截至时间',
                           max_length=100,
                           default="11:00")
    description = models.CharField('房间描述',
                                   max_length=1000,
                                   blank=True)
    status = models.BooleanField('开放状态', default=False)

    class Meta:
        verbose_name = "时间表"
        verbose_name_plural = "时间表"


class RoomAndTeacher(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name='房间名称')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='教师名称')
    status = models.IntegerField('状态')

    class Meta:
        verbose_name = '教师房间信息管理'
        verbose_name_plural = '教师房间信息管理'


class RoomAndStudent(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name='房间名称')
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='学生')
    status = models.IntegerField('状态')

    class Meta:
        verbose_name = '学生房间信息管理'
        verbose_name_plural = '学生房间信息管理'
    # 0 表示已通过，1 表示申请中， 2表示已移除


class ListOfForbiddenStudents(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name='房间名称')
    user = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='学生')

    class Meta:
        verbose_name = "禁言学生管理"
        verbose_name_plural = '禁言学生管理'
