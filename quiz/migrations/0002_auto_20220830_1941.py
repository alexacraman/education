# Generated by Django 3.2 on 2022-08-30 19:41

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='expired',
            field=models.DateField(default=datetime.datetime(2022, 8, 30, 19, 41, 33, 634073)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]