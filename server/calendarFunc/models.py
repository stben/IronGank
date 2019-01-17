from teacher.models import *

# Create your models here.


class Calendar():

    def start_bigger_than_end(self, start_time, end_time):
        start_int = int(start_time.split(":")[0])
        end_int = int(end_time.split(":")[0])
        return start_int > end_int

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
                                        })
                time_no = time_no + 1
            data = {'code': '0000', 'timeTableList': time_table_list}
            return data
        except Exception:
            data = {'code': '0001', 'msg': '未知错误'}
            return data

    def add_new_timetable(self, new_timetable_info):
        try:
            its_room_id = int(new_timetable_info.get('room_no'))
            its_room = Room.objects.get(id=its_room_id)
            if self.start_bigger_than_end(
                    new_timetable_info.get('begin'),
                    new_timetable_info.get('end')):
                data = {'code': '0001', 'msg': '创建失败，课程起始时间出错'}
                return data
            TimeTable.objects.create(
                room=its_room,
                class_week=new_timetable_info.get('week'),
                class_day=new_timetable_info.get('weekday'),
                begin=new_timetable_info.get('begin'),
                end=new_timetable_info.get('end'),
                description=new_timetable_info.get('description'),
                status=False,
            )
            data = {'code': '0000',
                    'roomNo': new_timetable_info.get('room_no'),
                    'week': new_timetable_info.get('week'),
                    'weekday': new_timetable_info.get('weekday'),
                    'begin': new_timetable_info.get('begin'),
                    'end': new_timetable_info.get('end'),
                    'description': new_timetable_info.get('description'),
                    }
            return data
        except Exception:
            data = {'code': '0001', 'msg': '创建失败'}
            return data

    def delete_timetable(self, delete_timetable_info):
        try:
            delete_timetable_id = int(
                delete_timetable_info.get('time_table_id'))
            delete_timetable = TimeTable.objects.get(id=delete_timetable_id)
            delete_timetable.delete()
            data = {'code': '0000', 'msg': '删除成功'}
            return data
        except Exception:
            data = {'code': '0001', 'msg': '课程安排不存在，请重试'}
            return data

    def modify_timetable(self, new_info):
        try:
            if self.start_bigger_than_end(
                    new_info.get('begin'), new_info.get('end')):
                data = {'code': '0001', 'msg': '修改失败，课程起始时间出错'}
                return data
            old_timetable = TimeTable.objects.get(
                id=int(new_info.get('time_table_id')),
            )
            if not old_timetable:
                data = {'code': '0002', 'msg': '修改失败，时间表不存在'}
                return data
            old_timetable.class_week = int(new_info.get('week'))
            old_timetable.class_day = int(new_info.get('weekday'))
            old_timetable.begin = new_info.get('begin')
            old_timetable.end = new_info.get('end')
            old_timetable.description = new_info.get('description')
            old_timetable.save()
            data = {'code': '0000', 'msg': '修改成功'}
            return data
        except BaseException:
            data = {'code': '0003', 'msg': '修改失败，未知错误'}
            return data
