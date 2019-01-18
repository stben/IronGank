"""teacher initialize"""
from django.apps import AppConfig
import os

default_app_config = 'teacher.IndexConfig'


def get_current_app_name(_file):
    """the function of getting current app name"""
    return os.path.split(os.path.dirname(_file))[-1]


class IndexConfig(AppConfig):
    """the class of index config"""
    name = get_current_app_name(__file__)
    verbose_name = '后台教师部分管理'
