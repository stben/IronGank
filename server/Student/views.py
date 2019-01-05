from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User,auth
from .models import Student
from django.db import transaction
import json

# Create your views here.


def register(request):
    if request.method == 'POST':
        try:
            with transaction.atomic():
                sid = request.POST.get('student_id')
                password = request.POST.get('password')
                tel = request.GET.get('tel')
                try:
                    user = User.objects.create_user(username=tel, password=password)
                except Exception:
                    data = {'code': '0001', 'msg': '手机号输入错误，请重新输入'}
                    return HttpResponse(json.dumps(data))
                student = Student(sid=sid, User=user)
                student.save()
                data = {'code': '0000', 'msg': '注册成功'}
                return HttpResponse(json.dumps(data))
        except Exception:
            data = {'code': '0001', 'msg': '学号输入错误，请重新输入'}
            return HttpResponse(json.dumps(data))


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            data = {'code': '0000', 'msg': '注册成功'}
            return HttpResponse(json.dumps(data))
        else:
            data = {'code': '0001', 'msg': '用户名或者密码错误'}
            return HttpResponse(json.dumps(data))


def student_logout(request):
    auth.logout(request)
    data = {'code': '0000', 'msg': '退出成功'}
    return HttpResponse(json.dumps(data))
