from django.http import JsonResponse
from calendar.models import Calendar
# Create your views here.


def get_list_of_timetable(request):
    if request.method == 'POST':
        room_no = request.POST.get('roomNo')
        calendar = Calendar()
        data = calendar.get_list_of_timetable(room_no)
        return JsonResponse(data)


def add_new_timetable(request):
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
        data = calendar.add_new_timetbale(new_timetable_info)
        return JsonResponse(data)
