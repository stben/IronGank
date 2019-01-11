from Teacher.models import *

# Create your models here.


class Calendar():
    def get_list_of_timetable(self, room_no):
        try:
            room = Room.objects.get(id=int(room_no))
            list_of_timetable = TimeTable.objects.filter(room=room)
            time_no = 1
            time_table_list = []
            for time_table in list_of_timetable:
                time_table_list.append({'roomNo': room_no,
                                        'timeTableId': time_table.id,
                                        'timeNo': time_no,
                                        'week': time_table.class_week,
                                        'weekday': time_table.class_day,
                                        'begin': time_table.begin,
                                        'end': time_table.end,
                                        'description': time_table.description,
                                        'status': time_table.status,
                                        })
                time_no = time_no + 1
            data = {'code': '0000', 'time_table_list': time_table_list}
            return data
        except Exception:
            print(Exception.message)
            data = {'code': '0001', 'msg': '未知错误'}
            return data
