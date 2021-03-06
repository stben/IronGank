"""the test is used to test the calendar"""
from django.test import TestCase
from teacher.models import College
from teacher.models import Room
from teacher.models import TimeTable
from calendarFunc.models import Calendar


class CalendarTestCase(TestCase):
    """the class of calendar test"""
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
        """the function of testing calendar can get all"""
        calendar = Calendar()
        room_no = '1'
        data = calendar.get_list_of_timetable(room_no)
        self.assertEqual(data.get('code'), '0000')

    def test_calendar_can_delete(self):
        """ the function of testing calendar can be deleted"""
        print(TimeTable.objects.get(id=1))
        calendar = Calendar()
        delete_timetable_info = {'room_no': '1',
                                 'time_no': '1',
                                 'time_table_id': '1', }
        data = calendar.delete_timetable(delete_timetable_info)
        self.assertEqual(data.get('code'), '0000')

    def test_calendar_can_modify(self):
        """the function of testing calendar can be modified"""
        calendar = Calendar()
        new_info = {'room_no': '1',
                    'week': '2',
                    'weekday': '6',
                    'begin': '13:00',
                    'end': '14:00',
                    'description': '图形学答疑',
                    'time_no': '1',
                    'time_table_id': '1',
                    'status': '0'}
        data = calendar.modify_timetable(new_info)
        self.assertEqual(data.get('code'), '0000')
