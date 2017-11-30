import os
import re
import time

from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import register
from django.urls import reverse


def add_test_user(user: User):
    user = User.objects.create_user('admin', 'admin@icare.com', 'admin', is_superuser=True)
    user = User.objects.create_user('test', 'test@icare.com', 'test')


COORDINATE_RATE = 60.0


def num_to_coord(num: float) -> str:
    """
    float to coordinate:浮点数到经纬度
    :param num:
    :return:
    """
    temp_num = num
    int_value = int(num)
    temp_num -= int_value
    minute = int(temp_num * COORDINATE_RATE)
    temp_num = temp_num * COORDINATE_RATE - minute
    second = temp_num * COORDINATE_RATE
    coor = "{0}°{1}'{2}\"".format(int_value, minute, round(second, 2))
    return coor


def coord_to_num(coor: str) -> float:
    """
    coordinate to num:经纬度到浮点数
    :param coor:
    :return:
    """
    items = re.split('°|\'|\"', coor)
    if (len(items) != 3):
        return -1
    int_value = int(items[0])
    minute = float(items[1])
    second = float(items[2])
    minute = minute + second / COORDINATE_RATE

    num = minute / COORDINATE_RATE + int(int_value)
    return num


@register.filter
def get_media_file_url(file_name):
    """
    获取文件URL
    :param file_name:
    :return:
    """
    return "{0}{1}{2}".format(reverse("backend:index"), settings.MEDIA_URL, file_name)


def get_media_file_path(file_name: str) -> str:
    """
    获取文件保存绝对路径
    :param file_name:
    :return:
    """
    return "{0}{1}".format(settings.MEDIA_ROOT, file_name)


def get_media_save_path(file_name):
    """
    获取文件原保存 新文件名 和 新绝对路径
    :param file_name:
    :return:
    """
    """:type:int"""
    t = int(time())

    file, ext = os.path.splitext(file_name)
    new_name = "{0}_{1}{2}".format(file, t, ext)
    return new_name, get_media_file_path(new_name)


@register.filter
def get_media_file_url(file_name):
    """
    获取文件URL
    :param file_name:
    :return:
    """
    return "{0}{1}{2}".format(reverse("backend:index"), settings.MEDIA_URL, file_name)


def get_media_file_path(file_name: str) -> str:
    """
    获取文件保存绝对路径
    :param file_name:
    :return:
    """
    return "{0}{1}".format(settings.MEDIA_ROOT, file_name)


def get_media_save_path(file_name):
    """
    获取文件原保存 新文件名 和 新绝对路径
    :param file_name:
    :return:
    """
    """:type:int"""
    t = int(time.time())

    file, ext = os.path.splitext(file_name)
    new_name = "{0}_{1}{2}".format(file, t, ext)
    return new_name, get_media_file_path(new_name)


def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        end_time = time.time()
        print("/*** Invoke :{0} ,elapsed:{1:.2f} ms **/".format(func.__name__, (end_time - start_time) * 1000))
        return r

    return wrapper


def log_time_request(func):
    def wrapper(request, *args, **kwargs):
        start_time = time.time()
        r = func(*args, **kwargs)
        end_time = time.time()
        print("/*** Invoke :{0} ,elapsed:{1:.2f} ms **/".format(func.__name__, (end_time - start_time) * 1000))
        return r

    return wrapper
