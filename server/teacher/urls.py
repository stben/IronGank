"""teacher urls"""
from django.urls import path
from teacher.views import teacher_login
from teacher.views import teacher_logout
from teacher.views import create_new_room
from teacher.views import all_room
from teacher.views import get_view_rooms
from teacher.views import get_room_info
from teacher.views import get_student_in_room
from teacher.views import ban_stu_list
from teacher.views import teacher_room

from calendarFunc.views import get_list_of_timetable
from calendarFunc.views import add_new_timetable
from calendarFunc.views import delete_timetable
from calendarFunc.views import modify_timetable

urlpatterns = [
    path('teacherLogin', teacher_login),
    path('teacherLogout', teacher_logout),
    path('newRoom', create_new_room),
    path('allRoom', all_room),
    path('teacherIndex', get_view_rooms),
    path('roomInfo', get_room_info),
    path('pickStudent', get_student_in_room),

    path('timeTable', get_list_of_timetable),
    path('newTimeTable', add_new_timetable),
    path('deleteTimeTable', delete_timetable),
    path('modifyTimeTable', modify_timetable),
    path('banStudent', ban_stu_list),
    path('pickTeacher', teacher_room)
]
