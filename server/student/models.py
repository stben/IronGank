"""student models"""
from django.db import models
from random import choice
import requests
import json
from django.contrib.auth.models import User


class Student(models.Model):
    """the class of student"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sid = models.CharField(max_length=20)

    def __str__(self):
        return User.objects.get(id=self.user_id).username


class YunPian(object):
    """the class of yun pian"""
    def __init__(self):
        self.APIKEY = "2c5f71b0dcda3c494893430c577b5225"
        self.single_send_url =\
            'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        parmas = {
            'apikey': self.APIKEY,
            'mobile': mobile,
            'text': '【郑绪祺】您的验证码是' + code + '。如非本人操作，请忽略本短信'
        }
        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


class SendMsg(object):
    """the class of send message"""
    def send_msg(self, mobile):
        """the function of sending message"""
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        code = "".join(random_str)
        print(code)
        yun_pian = YunPian()
        sms_status = yun_pian.send_sms(code, mobile)
        print(sms_status)
        if sms_status['code'] == 0:
            data = {'code': '0000', 'msg': code}
        else:
            data = {'code': '0001', 'msg': "发送失败"}
        return data
