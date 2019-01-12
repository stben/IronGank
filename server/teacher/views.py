from django.contrib.auth.models import auth
from django.http import HttpResponse
import re
import json
from teacher.models import *
from django.db import transaction
from django.http import JsonResponse
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
            data = {'code': '0001', 'msg': '用户名或者密码错误'}
            return HttpResponse(json.dumps(data))
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


def all_room(request):
    if request.method == 'GET':
        room = Room.objects.all()
        all_room_list = []
        for i in room:
            all_room_list.append({"roomNo": i.id,
                                  "roomName": i.name,
                                  "departmentName": i.college.name,
                                  "roomDescription": i.description})
        data = {'code': '0000', 'msg': '获取成功', 'allRoomList': all_room_list}
        return JsonResponse(data)


def get_view_rooms(request):
    if request.method == 'GET':
        username = request.user.username
        user = User.objects.filter(username=username)
        if not user:
            data = {'code': '0001', 'msg': '你的账号已注销或未登录'}
            return HttpResponse(json.dumps(data))
        rooms = RoomAndTeacher.objects.filter(user=user[0])
        room_list = []
        for item in rooms:
            room_list.append({'roomId': item.room.id,
                              'name': item.room.name,
                              'college': item.room.college.name})
        data = {'code': '0000', 'roomList': room_list}
        return HttpResponse(json.dumps(data))


def get_room_info(request):
    if request.method == 'GET':
        room_id = request.GET.get('roomId')
        room_list = Room.objects.filter(id=room_id)
        if not room_list:
            data = {'code': '0001', 'msg': '你的房间不存在或已注销'}
            return HttpResponse(json.dumps(data))
        room = room_list[0]
        data = {'code': '0000', 'msg': '获取成功', 'roomName': room.name, 'roomId': room.id,
                'departmentName': room.college.name, 'password': room.password, 'roomDescription': room.description,
                'isWhiteboard': room.is_need_code_editor, 'isCode': room.is_need_code_editor,
                'isPassword': room.is_need_password}
        return HttpResponse(json.dumps(data))
    if request.method == 'POST':
        room_id = int(request.POST.get('roomId'))
        room_name = request.POST.get('roomName')
        college_name = request.POST.get('departmentName')
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
        college = College.objects.filter(name=college_name)
        if not college:
            data = {'code': '0003', 'msg': '请输入正确院系'}
            return HttpResponse(json.dumps(data))
        try:
            room = Room.objects.get(id=room_id)
            room.name = room_name
            room.college = college[0]
            room.password = password
            room.description = description
            room.is_need_password = is_need_password
            room.is_need_code_editor = is_need_code_editor
            room.is_need_whiteboard = is_need_whiteboard
            room.save
            data = {'code': '0000', 'msg': '保存成功'}
            return HttpResponse(json.dumps(data))
        except BaseException:
            data = {'code': '0004', 'msg': '未知错误，请联系管理员'}
            return HttpResponse(json.dumps(data))


def get_student_in_room(request):
    if request.method == 'GET':
        room_id = int(request.GET.get('roomNo'))
        room_list = Room.objects.filter(id=room_id)
        if not room_list:
            data = {'code': '0001', 'msg': '你的房间不存在或已注销'}
            return HttpResponse(json.dumps(data))
        stu_list = RoomAndStudent.objects.filter(room=room_list[0])
        audit_list = []
        accept_list = []
        for stu in stu_list:
            if stu.status == 1:
                audit_list.append(
                    {'stuName': stu.student.user.get_full_name(), 'stuNo': stu.student.sid})
            if stu.status == 0:
                accept_list.append(
                    {'stuName': stu.student.user.get_full_name(), 'stuNo': stu.student.sid})
        data = {
            'code': '0000',
            'auditList': audit_list,
            'acceptedList': accept_list}
        return HttpResponse(json.dumps(data))
    if request.method == 'POST':
        room_id = int(request.POST.get('roomNo'))
        sid = request.POST.get('stuNo')
        is_done = request.POST.get('isAccepted')
        stu_list = Student.objects.filter(sid=sid)
        if not stu_list:
            data = {'code': '0001', 'msg': '学生不存在或已注销'}
            return HttpResponse(json.dumps(data))
        room_list = Room.objects.filter(id=room_id)
        if not room_list:
            data = {'code': '0002', 'msg': '房间不存在或已注销'}
            return HttpResponse(json.dumps(data))
        try:
            stu_in = RoomAndStudent.objects.get(room=room_list[0], student=stu_list[0])
        except:
            data = {'code': '0003', 'msg': '记录不存在或已注销'}
            return HttpResponse(json.dumps(data))
        if stu_in.status == 1:
            if is_done == '1':
                stu_in.status = 0  # 如果申请通过，变成在班级学生
                stu_in.save()
                data = {'code': '0000', 'msg': '通过申请'}
                return HttpResponse(json.dumps(data))
            else:
                stu_in.status = 2  # 如果申请不通过，变成注销班级学生
                stu_in.save()
                data = {'code': '0000', 'msg': '拒绝申请'}
                return HttpResponse(json.dumps(data))
        else:
            if is_done == '0':
                stu_in.status = 2   # 如果已在班级，移除学生
                stu_in.save()
                data = {'code': '0000', 'msg': '成功移除'}
                return HttpResponse(json.dumps(data))
            else:
                data = {'code': '0004', 'msg': '学生已通过或已移除'}
                return HttpResponse(json.dumps(data))


def ban_stu_list(request):
    if request.method == 'GET':
        try:
            ban_student_lists = ListOfForbiddenStudents.objects.all()
            ban_list = []
            for i in ban_student_lists:
                student = Student.objects.get(user=i.user)
                ban_list.append({"stuNo": student.sid,
                                 "stuName": i.user.get_full_name(),
                                 })
            data = {'code': '0000', 'sum': len(ban_list), 'banList': ban_list}
            return JsonResponse(data)
        except Exception:
            print(Exception.message)
            data = {'code': '0001', 'msg': '未知错误'}
            return data
    if request.method == 'POST':
        try:
            room_id = int(request.POST.get('roomNo'))
            user_id = request.POST.get('stuNo')
            its_student = Student.objects.get(sid=user_id)
            its_room = Room.objects.get(id=room_id)
            re_user = its_student.user
            ListOfForbiddenStudents.objects.filter(
                room_id=its_room, user_id=re_user).delete()
            data = {'code': '0000', 'msg': '删除成功'}
            return JsonResponse(data)
        except Exception:
            print(Exception.message)
            data = {'code': '0001', 'msg': '未知错误'}
            return data
