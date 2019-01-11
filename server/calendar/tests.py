from django.test import TestCase
from django.test import Client

from Teacher.models import *
from calendar.models import *


class CalendarTestCase(TestCase):
    def setUp(self):
        college = College.objects.create(id=1, name='软件', college_id=1)
        room = Room.objects.create(
            id=1,
            name="图形学",
            college=college,
            password='1',
            description='1',
            is_need_code_editor=True,
            is_need_password=True,
            is_need_whiteboard=True)
        TimeTable.objects.create(
            id=1,
            room=room,
            class_week="1",
            class_day='1',
            begin="13:00",
            end="14:00",
            description="图形学",
            status=0)

    def test_calendar_can_get_all(self):
        calendar = Calendar()
        room_no = '1'
        data = calendar.get_list_of_timetable(room_no)
        self.assertEqual(data.get('code'), '0000')

    def test_calendar_can_delete(self):
        print(TimeTable.objects.get(id=1))
        calendar = Calendar()
        delete_timetable_info = {'room_no': '1',
                                 'time_no': '1',
                                 'time_table_id': '1', }
        data = calendar.delete_timetable(delete_timetable_info)
        self.assertEqual(data.get('code'), '0000')
