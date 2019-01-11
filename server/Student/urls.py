from django.urls import path
from Student.views import *

urlpatterns = [
    path('register', register),
    path('studentLogin', student_login),
    path('studentLogout', student_logout),
]
