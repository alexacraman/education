# Generated by Django 3.2 on 2022-09-05 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_usersession_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='loggedout',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
