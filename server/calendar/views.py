from django.http import JsonResponse
from calendar.models import Calendar
# Create your views here.


def get_list_of_timetable(request):
    if request.method == 'POST':
        room_no = request.POST.get('roomNo')
        calendar = Calendar()
        data = calendar.get_list_of_timetable(room_no)
        return JsonResponse(data)
