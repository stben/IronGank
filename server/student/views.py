"""student views"""
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth
from .models import SendMsg
from .models import Student
from teacher.models import Room
from teacher.models import RoomAndTeacher
from teacher.models import RoomAndStudent
from django.db import transaction
import json


def register(request):
    """the function of register"""
    if request.method == 'POST':
        try:
            with transaction.atomic():
                sid = request.POST.get('student_id')
                password = request.POST.get('password')
                tel = request.POST.get('tel')
                first_name = request.POST.get('firstName')
                new_user = User.objects.create_user(
                    username=tel,
                    password=password,
                    first_name=first_name)
                student = Student(sid=sid, user=new_user)
                student.save()
                data = {'code': '0000', 'msg': '注册成功'}
                return HttpResponse(json.dumps(data))
        except Exception:
            data = {'code': '0001', 'msg': '手机号已注册'}
            return HttpResponse(json.dumps(data))


def student_login(request):
    """the function of student login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        if len(username) != 11:
            data = {'code': '0002',
                    'msg': '请输入正确格式的用户名（手机号）'}
            return HttpResponse(json.dumps(data))
        password = request.POST.get('password')
        user = auth.authenticate(username=username,
                                 password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            data = {'code': '0000', 'msg': '登录成功'}
            return HttpResponse(json.dumps(data))
        else:
            data = {'code': '0001', 'msg': '用户名或者密码错误'}
            return HttpResponse(json.dumps(data))


def student_logout(request):
    """the function of student logout"""
    auth.logout(request)
    data = {'code': '0000', 'msg': '退出成功'}
    return HttpResponse(json.dumps(data))


def get_rooms(request):
    """the function of getting rooms"""
    if request.method == 'GET':
        try:
            rooms = Room.objects.filter()
            all_rooms = []
            for i in rooms:
                all_rooms.append({"roomNo": i.id, "roomName": i.name,
                                  "departmentName": i.college.name,
                                  "roomDescription": i.description,
                                  'isPassword': i.is_need_password,
                                  'password': i.password})
            data = {'code': '0000',
                    'msg': '获取成功',
                    'allRooms': all_rooms}
            return JsonResponse(data)
        except BaseException:
            data = {'code': '0001', 'msg': '未知错误'}
            return JsonResponse(data)


def add_student_room(request):
    """the function of adding student room"""
    if request.method == 'GET':
        try:
            room_id = request.GET.get('roomNo')
            user = request.user
            if not user:
                data = {'code': '0001', 'msg': '你已经登出或未登录'}
                return HttpResponse(json.dumps(data))
            rooms = Room.objects.filter(id=int(room_id))
            if not rooms:
                data = {'code': '0002', 'msg': '房间不存在'}
                return HttpResponse(json.dumps(data))
            students = Student.objects.filter(user=user)
            if students:
                student_rooms = RoomAndStudent.objects.filter(
                    student=students[0], room=rooms[0])
                if student_rooms:
                    data = {'code': '0003', 'msg': '你已经申请'}
                    return HttpResponse(json.dumps(data))
                student_room = RoomAndStudent(
                    student=students[0], room=rooms[0], status=1)
                student_room.save()
                data = {'code': '0000', 'msg': '申请成功'}
                return HttpResponse(json.dumps(data))
            else:
                teacher_rooms = RoomAndTeacher.objects.filter(
                    user=user, room=rooms[0]
                )
                if teacher_rooms:
                    data = {'code': '0003', 'msg': '你已经申请'}
                    return HttpResponse(json.dumps(data))
                teacher_room = RoomAndTeacher(
                    user=user, room=rooms[0], status=3)
                teacher_room.save()
                data = {'code': '0000', 'msg': '申请成功'}
                return HttpResponse(json.dumps(data))
        except BaseException:
            data = {'code': '0003', 'msg': '未知错误'}
            return HttpResponse(json.dumps(data))


def student_enter(request):
    """the function of student enter"""
    if request.method == 'GET':
        try:
            room_id = request.GET.get('roomNo')
            rooms = Room.objects.filter(id=int(room_id))
            students = Student.objects.filter(user=request.user)
            if not rooms:
                data = {'code': '0001', 'msg': '房间不存在'}
                return HttpResponse(json.dumps(data))
            student_in = RoomAndStudent.objects.filter(
                room=rooms[0], student=students[0])
            data = {'code': '0000',
                    'myNo': students[0].sid,
                    'myName': students[0].user.first_name,
                    'myStatus': student_in[0].status,
                    'roomNo': room_id,
                    'roomName': rooms[0].name}
            return HttpResponse(json.dumps(data))
        except BaseException:
            data = {'code': '0002', 'msg': '未知错误'}
            return HttpResponse(json.dumps(data))


def send_msg(request):
    """ the function of sending message """
    if request.method == 'POST':
        try:
            mobile = request.POST.get('mobile')
            if mobile != '':
                send_class = SendMsg()
                data = send_class.send_msg(mobile)
            else:
                data = {'code': '0001', 'msg': '手机号格式有误！'}
            return JsonResponse(data)
        except Exception:
            data = {'code': '0001', 'msg': '手机号格式有误！'}
            return JsonResponse(data)
