# Generated by Django 3.0 on 2019-12-18 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0013_auto_20191218_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercices',
            name='nombre_salaries',
        ),
    ]
