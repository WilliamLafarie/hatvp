# Generated by Django 3.0 on 2020-01-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0021_auto_20200127_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decisions_concernees',
            name='decision_concernee',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='code_postal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='denomination',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='page_facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='page_linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='page_twitter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='pays',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='site_web',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='type_identifiant_national',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='informations_generales',
            name='ville',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
