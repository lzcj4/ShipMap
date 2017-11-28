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
    class Meta:
        default_permissions = ()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserInfo.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userinfo.save()


# endregion


# region ship models

class Ship(models.Model):
    """
    船只
    """
    no = models.CharField(max_length=100, verbose_name='船只编号', unique=True)
    name = models.CharField(max_length=100, verbose_name='船名', unique=False, default='')
    harbor = models.CharField(max_length=100, verbose_name='码头', unique=False, default='')
    caption = models.CharField(max_length=100, verbose_name='船长', unique=False, default='')
    phone = models.CharField(max_length=100, verbose_name='电话', unique=False, default='')
    address = models.CharField(max_length=100, verbose_name='地址', unique=False, default='')

    class Meta:
        default_permissions = ()


class ShipRoute(models.Model):
    """
    船只路线
    """
    ship = models.ForeignKey("Ship", on_delete=models.CASCADE)
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        default_permissions = ()


class ShipDefenceArea(models.Model):
    """
    船只防区
    """
    name = models.CharField(max_length=100, verbose_name='船名', unique=False, default='')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    radius = models.FloatField(verbose_name='防御半径')

    class Meta:
        default_permissions = ()


class Radar(models.Model):
    """
    雷达
    经纬度转换:
    https://wenku.baidu.com/view/26eda9146edb6f1aff001fe0.html
    http://www.gzhatu.com/du2dfm.html
    """
    no = models.CharField(max_length=100, verbose_name='雷达编号', unique=True)
    name = models.CharField(max_length=100, verbose_name='雷达名称', unique=False, default='')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    address = models.CharField(max_length=100, verbose_name='地址', unique=False, default='')

    class Meta:
        default_permissions = ()

# endregion
