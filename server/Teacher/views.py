from django.contrib.auth.models import auth
from django.http import HttpResponse
import re
import json
from Teacher.models import *
from django.db import transaction

# Create your views here.


def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if re.match(
            r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',
                username):
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                data = {'code': '0000', 'msg': '登录成功'}
                return HttpResponse(json.dumps(data))
            else:
                data = {'code': '0001', 'msg': '用户名或者密码错误'}
                return HttpResponse(json.dumps(data))
        else:
            data = {'code': '0002', 'msg': '请输入正确格式的用户名（邮箱）'}
            return HttpResponse(json.dumps(data))


def teacher_logout(request):
    auth.logout(request)
    data = {'code': '0000', 'msg': '退出成功'}
    return HttpResponse(json.dumps(data))


def create_new_room(request):
    if request.method == 'POST':
        room_name = request.POST.get('roomName')
        college_id = request.POST.get('departmentId')
        password = request.POST.get('password')
        description = request.POST.get('roomDescription')
        is_need_whiteboard = request.POST.get('isBoard')
        is_need_code_editor = request.POST.get('isCode')
        is_need_password = request.POST.get('isPassword')
        if is_need_password and password == '':
            data = {'code': '0001', 'msg': '请输入房间密码'}
            return HttpResponse(json.dumps(data))
        if room_name == '':
            data = {'code': '0002', 'msg': '请输入房间名称'}
            return HttpResponse(json.dumps(data))
        college = College.objects.filter(college_id=college_id)
        if not college:
            data = {'code': '0003', 'msg': '请输入正确院系'}
            return HttpResponse(json.dumps(data))
        username = request.user.username
        user = User.objects.filter(username=username)
        if not user:
            data = {'code': '0004', 'msg': '你的账号已注销或未登录'}
            return HttpResponse(json.dumps(data))
        try:
            with transaction.atomic():
                room = Room(name=room_name, college=college[0], password=password, description=description,
                            is_need_whiteboard=is_need_whiteboard, is_need_password=is_need_password,
                            is_need_code_editor=is_need_code_editor)
                room.save()
                owner = RoomAndTeacher(user=user, room=room, status=1)
                owner.save()
                data = {'code': '0000', 'msg': '创建成功'}
                return HttpResponse(json.dumps(data))
        except BaseException:
            data = {'code': '0005', 'msg': '未知错误请联系管理员'}
            return HttpResponse(json.dumps(data))
