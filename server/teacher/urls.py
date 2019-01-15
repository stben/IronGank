from django.urls import path
from teacher.views import *
from calendar.views import *

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
    path('banStudent', ban_stu_list)
]
