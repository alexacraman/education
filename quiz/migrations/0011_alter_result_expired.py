# Generated by Django 3.2 on 2022-09-22 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_alter_result_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='expired',
            field=models.DateField(),
        ),
    ]
