# Generated by Django 3.0 on 2019-12-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0016_auto_20191218_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercices',
            name='nombre_salaries',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
