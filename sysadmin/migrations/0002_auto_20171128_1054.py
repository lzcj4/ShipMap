# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=100, unique=True, verbose_name='雷达编号')),
                ('name', models.CharField(default='', max_length=100, verbose_name='雷达名称')),
                ('longitude', models.FloatField(verbose_name='经度')),
                ('latitude', models.FloatField(verbose_name='纬度')),
                ('address', models.CharField(default='', max_length=100, verbose_name='地址')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=100, unique=True, verbose_name='船只编号')),
                ('name', models.CharField(default='', max_length=100, verbose_name='船名')),
                ('harbor', models.CharField(default='', max_length=100, verbose_name='码头')),
                ('caption', models.CharField(default='', max_length=100, verbose_name='船长')),
                ('phone', models.CharField(default='', max_length=100, verbose_name='电话')),
                ('address', models.CharField(default='', max_length=100, verbose_name='地址')),
            ],
        ),
        migrations.RemoveField(
            model_name='markfeature',
            name='object',
        ),
        migrations.RemoveField(
            model_name='markfile',
            name='task',
        ),
        migrations.RemoveField(
            model_name='markobject',
            name='file',
        ),
        migrations.RemoveField(
            model_name='marktask',
            name='user_created',
        ),
        migrations.RemoveField(
            model_name='markusertask',
            name='task',
        ),
        migrations.RemoveField(
            model_name='markusertask',
            name='user',
        ),
        migrations.DeleteModel(
            name='MarkFeature',
        ),
        migrations.DeleteModel(
            name='MarkFile',
        ),
        migrations.DeleteModel(
            name='MarkObject',
        ),
        migrations.DeleteModel(
            name='MarkTask',
        ),
        migrations.DeleteModel(
            name='MarkUserTask',
        ),
    ]
