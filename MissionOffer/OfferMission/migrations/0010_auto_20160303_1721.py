# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfferMission', '0009_auto_20151025_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='status',
            field=models.CharField(choices=[('0', '待接收'), ('1', '进行中'), ('2', '待审核'), ('3', '已完成'), ('4', '失败')], default='0', max_length=20),
        ),
    ]
