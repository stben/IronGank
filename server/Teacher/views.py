from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.db import transaction
from Teacher.models import *
import re
import json

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
        # noinspection PyBroadException
        try:
            with transaction.atomic():
                room_name = request.POST.get('roomName')
                room_department_id = request.POST.get('departmentId')
                room_college = College.objects.filter(
                    college_id=room_department_id)[0]
                room_password = request.POST.get('password')
                room_description = request.POST.get('roomDescription')
                is_board = request.POST.get('isBoard')
                is_code = request.POST.get('isCode')
                is_need_password = request.POST.get('isPassword')
                room = Room(name=room_name,
                            college=room_college,
                            password = room_password,
                            description=room_description,
                            is_need_whiteboard=is_board,
                            is_need_code_editor=is_code,
                            is_need_password=is_need_password,
                            )
                room.save()
                data = {'code': '0000', 'msg': '新建房间成功！'}
                return HttpResponse(json.dumps(data))
        except Exception:
            data = {'code': '0001', 'msg': '创建失败！请检查字段格式！'}
            return HttpResponse(json.dumps(data))
