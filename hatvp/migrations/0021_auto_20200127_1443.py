# Generated by Django 3.0 on 2020-01-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0020_auto_20200127_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations_generales',
            name='adresse',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]