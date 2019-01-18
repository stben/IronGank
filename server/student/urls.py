from django.urls import path
from student.views import register
from student.views import student_login
from student.views import student_logout
from student.views import get_rooms
from student.views import add_student_room

urlpatterns = [
    path('register', register),
    path('studentLogin', student_login),
    path('studentLogout', student_logout),
    path('studentIndex', get_rooms),
    path('studentRoom', add_student_room),
]
