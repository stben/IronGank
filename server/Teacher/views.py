from django.http import HttpResponse
from django.contrib.auth.models import auth
import json
import re


# Create your views here.
def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', username):
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
