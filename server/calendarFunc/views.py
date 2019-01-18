"""calendar test views"""
from django.http import JsonResponse
from calendarFunc.models import Calendar


def get_list_of_timetable(request):
    """the function of getting list of timetable"""
    if request.method == 'POST':
        room_no = request.POST.get('roomNo')
        calendar = Calendar()
        data = calendar.get_list_of_timetable(room_no)
        return JsonResponse(data)


def add_new_timetable(request):
    """the function of adding new timetable"""
    if request.method == 'POST':
        room_no = request.POST.get('roomNo')
        week = request.POST.get('week')
        weekday = request.POST.get('weekday')
        begin = request.POST.get('begin')
        end = request.POST.get('end')
        description = request.POST.get('description')
        new_timetable_info = {
            'room_no': room_no,
            'week': week,
            'weekday': weekday,
            'begin': begin,
            'end': end,
            'description': description,
        }
        calendar = Calendar()
        data = calendar.add_new_timetable(new_timetable_info)
        return JsonResponse(data)


def delete_timetable(request):
    """the function of deleting timetable"""
    if request.method == 'POST':
        room_no = request.POST.get('roomNo')
        time_no = request.POST.get('timeNo')
        time_table_id = request.POST.get('timeTableId')
        info = {
            'room_no': room_no,
            'time_no': time_no,
            'time_table_id': time_table_id,
        }
        calendar = Calendar()
        data = calendar.delete_timetable(info)
        return JsonResponse(data)


def modify_timetable(request):
    """the function of modifying timetable"""
    if request.method == 'POST':
        time_table_id = request.POST.get('timeTableId')
        week = request.POST.get('week')
        weekday = request.POST.get('weekday')
        begin = request.POST.get('begin')
        end = request.POST.get('end')
        description = request.POST.get('description')
        new_info = {
            'time_table_id': time_table_id,
            'week': week,
            'weekday': weekday,
            'begin': begin,
            'end': end,
            'description': description,
        }
        calendar = Calendar()
        data = calendar.modify_timetable(new_info)
        return JsonResponse(data)
