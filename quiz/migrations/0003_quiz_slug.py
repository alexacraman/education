# Generated by Django 3.2 on 2022-08-30 21:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20220830_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2022, 8, 30, 21, 48, 43, 938582)),
            preserve_default=False,
        ),
    ]
