from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


# region  Sys-Auth models

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    # tasks = models.ForeignKey('MarkTask', on_delete=models.CASCADE, default=0)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userinfo.save()


# endregion


# region JS-Mark models

class MarkUserTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    task = models.ForeignKey('MarkTask', on_delete=models.CASCADE)


class MarkTask(models.Model):
    name = models.CharField(max_length=100, verbose_name='任务名', unique=False, default='')
    user_created = models.ForeignKey(User, verbose_name='创建人', null=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # class Meta:
    #     default_related_name = "files"
    #     permissions = (("create_marktask", "创建任务权利"))


class MarkFile(models.Model):
    file_name = models.CharField(max_length=100, verbose_name='文件名', default='')
    file_path = models.CharField(max_length=500, verbose_name='文件服务器端相对路径', default='')
    task = models.ForeignKey('MarkTask', on_delete=models.CASCADE, related_name='files')


class MarkObject(models.Model):
    name = models.CharField(max_length=100, verbose_name='对象名', default='')
    file = models.ForeignKey('MarkFile', on_delete=models.CASCADE, related_name='objects')


class MarkFeature(models.Model):
    name = models.CharField(max_length=100, verbose_name='特征名', default='')
    object = models.ForeignKey('MarkObject', on_delete=models.CASCADE, related_name='features')

# endregion
