"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from . import views
from Student.views import *
from Teacher.views import *

urlpatterns = [
    path('', views.index),
    path('api/', include([
        path('random/', views.random)]
    )),
    path('admin/', admin.site.urls),
    path('student/register', register),
    path('student/studentLogin', student_login),
    path('student/studentLogout', student_logout),
    path('teacher/teacherLogin', teacher_login),
    path('teacher/teacherLogout', teacher_logout),
    path('teacher/newRoom', create_new_room),
    path('teacher/allRoom', all_room),
    path('teacher/teacherIndex', get_view_rooms),
    path('teacher/roomInfo', get_room_info),
    path('teacher/pickRoomStudent', get_student_in_room)
]
