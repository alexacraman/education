# Generated by Django 3.2 on 2022-09-05 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_result_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='expired',
            field=models.DateField(default=datetime.datetime(2023, 9, 5, 15, 31, 48, 107449)),
        ),
    ]
