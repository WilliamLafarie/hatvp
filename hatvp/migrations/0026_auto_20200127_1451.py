# Generated by Django 3.0 on 2020-01-27 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hatvp', '0025_auto_20200127_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliations',
            name='identifiant_national_affiliation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='affiliations',
            name='type_identifiant_national_affiliation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='denomination_client',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='identifiant_national_client',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='type_identifiant_national_client',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='fonction_collaborateur',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='nom_collaborateur',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='nom_prenom_collaborateur',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='collaborateurs',
            name='prenom_collaborateur',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dirigeants',
            name='fonction_dirigeant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dirigeants',
            name='nom_dirigeant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dirigeants',
            name='nom_prenom_dirigeant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='dirigeants',
            name='prenom_dirigeant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='domaines_intervention',
            name='domaines_intervention_actions_menees',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='chiffre_affaires',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='montant_depense',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='exercices',
            name='nombre_salaries',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='objets_activites',
            name='identifiant_fiche',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
