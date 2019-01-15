from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User, auth
from .models import Student
from teacher.models import *
from django.db import transaction
import json

# Create your views here.


def register(request):
  if request.method == 'POST':
    try:
      with transaction.atomic():
        sid = request.POST.get('student_id')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        first_name = request.POST.get('firstName')
        new_user = User.objects.create_user(
          username=tel, password=password, first_name=first_name)
        student = Student(sid=sid, user=new_user)
        student.save()
        data = {'code': '0000', 'msg': '注册成功'}
        return HttpResponse(json.dumps(data))
    except Exception:
      data = {'code': '0001', 'msg': '手机号已注册'}
      return HttpResponse(json.dumps(data))



def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if len(username) != 11:
            data = {'code': '0002', 'msg': '请输入正确格式的用户名（手机号）'}
            return HttpResponse(json.dumps(data))
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            data = {'code': '0000', 'msg': '登录成功'}
            return HttpResponse(json.dumps(data))
        else:
            data = {'code': '0001', 'msg': '用户名或者密码错误'}
            return HttpResponse(json.dumps(data))


def student_logout(request):
    auth.logout(request)
    data = {'code': '0000', 'msg': '退出成功'}
    return HttpResponse(json.dumps(data))


def get_rooms(request):
    if request.methid == 'GET':
        rooms = Room.objects.filter()
        all_rooms = []
        for i in rooms:
            all_rooms.append({"roomNo": i.id, "roomName": i.name, "departmentName": i.college.name,
                              "roomDescription": i.description})
        data = {'code': '0000', 'msg': '获取成功', 'allRooms': all_rooms}
        return JsonResponse(data)


def add_student_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('roomNo')
        user = request.user
        students = Student.objects.filter(user=user)
        if not students:
            data = {'code': '0001', 'msg': '你已经登出或未登录'}
            return HttpResponse(json.dumps(data))
        rooms = Room.objects.filter(id=int(room_id))
        if not rooms:
            data = {'code': '0002', 'msg': '房间不存在'}
            return HttpResponse(json.dumps(data))
        try:
            student_room = RoomAndStudent(
                student=students[0], room=rooms[0], status=1)
            student_room.save()
            data = {'code': '0000', 'msg': '申请成功'}
            return HttpResponse(json.dumps(data))
        except BaseException:
            data = {'code': '0003', 'msg': '未知错误'}
            return HttpResponse(json.dumps(data))
