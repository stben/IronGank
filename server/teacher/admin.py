from django.contrib import admin
from teacher.models import *


admin.site.site_title = '后台管理'
admin.site.site_header = '后台管理'
# Register your models here.


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['college_id', 'name', ]
    search_fields = ['college_id', 'name', ]
    list_filter = ['college_id', 'name', ]
    ordering = ['college_id']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'college', 'password', 'description', 'is_need_whiteboard',
                    'is_need_code_editor', 'is_need_password']


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ['room', 'class_week', 'class_day', 'begin', 'end',
                    'description', 'status']


@admin.register(RoomAndTeacher)
class RoomAndTeacherAdmin(admin.ModelAdmin):
    list_display = ['room', 'user', 'status']


@admin.register(RoomAndStudent)
class RoomAndStudentAdmin(admin.ModelAdmin):
    list_display = ['room', 'student', 'status']


@admin.register(ListOfForbiddenStudents)
class ListOfForbiddenStudentsAdmin(admin.ModelAdmin):
    list_display = ['room', 'user']
