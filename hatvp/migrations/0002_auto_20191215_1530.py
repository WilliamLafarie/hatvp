# Generated by Django 3.0 on 2019-12-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_generales',
            name='declaration_organisation_appartenance',
            field=models.BooleanField(null=True),
        ),
    ]
