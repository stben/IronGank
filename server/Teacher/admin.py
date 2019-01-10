from django.contrib import admin
from Teacher.models import *


# Register your models here.
admin.site.register(College)
admin.site.register(Room)
admin.site.register(RoomAndTeacher)
admin.site.register(RoomAndStudent)
admin.site.register(TimeTable)
admin.site.register(ListOfForbiddenStudents)
