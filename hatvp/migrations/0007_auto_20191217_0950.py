# Generated by Django 3.0 on 2019-12-17 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0006_auto_20191216_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercices',
            name='declaration_incomplete',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='exercice_sans_CA',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='exercice_sans_activite',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Secteur_activites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secteur_activite', models.CharField(max_length=200)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Informations_generales')),
            ],
        ),
    ]
