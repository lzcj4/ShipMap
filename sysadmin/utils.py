import os

from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import register
from django.urls import reverse
import time
from sysadmin.models import MarkTask, MarkFile, MarkUserTask


def add_test_user(user: User):
    pass
    # user = User.objects.create_user('test', 'test@icare.com', 'test')
    # if not user:
    #     user.set_password("admin")
    #     user.save()


def add_test_task(user: User):
    get_items = MarkUserTask.objects.filter(user=user)
    # u_t = MarkUserTask.objects.get(user__id=user.id)
    u_t = get_items[0] if get_items and len(get_items) > 0 else None
    if u_t:
        print("user:{0},task:{1}".format(u_t.user.id, u_t.task.id))
    task = MarkTask(name="task1")
    task.save()

    file = MarkFile(file_path='c:/test.jpg')
    file.task = task
    file.save()

    user_task = MarkUserTask(task=task, user=user)
    user_task.save()
    file2 = MarkFile(file_path='c:/test2.jpg')
    file2.task = task
    file2.save()

    print("task:{0},file:{1},task.files:{2}".format(task.id, file.id, task.files.count()))

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
