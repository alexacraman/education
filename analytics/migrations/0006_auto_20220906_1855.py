# Generated by Django 3.2 on 2022-09-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20220906_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersession',
            name='total',
        ),
        migrations.DeleteModel(
            name='ObjectViewed',
        ),
    ]
