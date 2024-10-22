# Generated by Django 3.0 on 2019-12-15 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercices',
            fields=[
                ('exercices_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_debut', models.CharField(max_length=200)),
                ('date_fin', models.CharField(max_length=200)),
                ('exercice_sans_activite', models.BooleanField()),
                ('nombre_activites', models.IntegerField()),
                ('declaration_incomplete', models.BooleanField()),
                ('date_publication', models.CharField(max_length=200)),
                ('exercice_sans_CA', models.BooleanField()),
                ('montant_depense', models.CharField(max_length=200)),
                ('nombre_salaries', models.FloatField()),
                ('chiffre_affaires', models.CharField(max_length=200)),
                ('annee_debut', models.IntegerField()),
                ('annee_fin', models.IntegerField()),
                ('montant_depense_inf', models.IntegerField()),
                ('montant_depense_sup', models.IntegerField()),
                ('ca_inf', models.IntegerField()),
                ('ca_sup', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Info_generales',
            fields=[
                ('representants_id', models.IntegerField(primary_key=True, serialize=False)),
                ('adresse', models.CharField(max_length=200)),
                ('code_postal', models.CharField(max_length=200)),
                ('derniere_publication_activite', models.CharField(max_length=200)),
                ('date_premiere_publication', models.CharField(max_length=200)),
                ('declaration_organisation_appartenance', models.BooleanField()),
                ('declaration_tiers', models.BooleanField()),
                ('denomination', models.CharField(max_length=200)),
                ('identifiant_national', models.CharField(max_length=200)),
                ('activites_publiees', models.BooleanField()),
                ('page_facebook', models.CharField(max_length=200)),
                ('page_linkedin', models.CharField(max_length=200)),
                ('page_twitter', models.CharField(max_length=200)),
                ('site_web', models.CharField(max_length=200)),
                ('nom_usage_HATVP', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=200)),
                ('sigle_HATVP', models.CharField(max_length=200)),
                ('type_identifiant_national', models.CharField(max_length=200)),
                ('ville', models.CharField(max_length=200)),
                ('label_categorie_organisation', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Objets_activites',
            fields=[
                ('activite_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_publication_activite', models.CharField(max_length=200)),
                ('identifiant_fiche', models.CharField(max_length=200)),
                ('objet_activite', models.CharField(max_length=200)),
                ('exercices_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Exercices')),
            ],
        ),
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('action_representation_interet_id', models.IntegerField(primary_key=True, serialize=False)),
                ('observation', models.CharField(max_length=200)),
                ('activite_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Objets_activites')),
            ],
        ),
        migrations.CreateModel(
            name='Niveaux_interventions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_intervention', models.CharField(max_length=200)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Info_generales')),
            ],
        ),
        migrations.AddField(
            model_name='exercices',
            name='representants_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Info_generales'),
        ),
        migrations.CreateModel(
            name='Domaines_interventions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domaines_intervention_actions_menees', models.CharField(max_length=200)),
                ('activite_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Objets_activites')),
            ],
        ),
        migrations.CreateModel(
            name='Dirigeants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite_dirigeant', models.CharField(max_length=200)),
                ('fonction_dirigeant', models.CharField(max_length=200)),
                ('nom_dirigeant', models.CharField(max_length=200)),
                ('prenom_dirigeant', models.CharField(max_length=200)),
                ('nom_prenom_dirigeant', models.CharField(max_length=200)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Info_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Decisions_concernees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision_concernee', models.CharField(max_length=200)),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Observations')),
            ],
        ),
        migrations.CreateModel(
            name='Collaborateurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('civilite_collaborateur', models.CharField(max_length=200)),
                ('fonction_collaborateur', models.CharField(max_length=200)),
                ('nom_collaborateur', models.CharField(max_length=200)),
                ('prenom_collaborateur', models.CharField(max_length=200)),
                ('nom_prenom_collaborateur', models.CharField(max_length=200)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Info_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination_client', models.CharField(max_length=200)),
                ('identifiant_national_client', models.CharField(max_length=200)),
                ('type_identifiant_national_client', models.CharField(max_length=200)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Info_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiaires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beneficiaire_action_menee', models.CharField(max_length=200)),
                ('action_menee_en_propre', models.IntegerField()),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Observations')),
            ],
        ),
        migrations.CreateModel(
            name='Affiliations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination_affiliation', models.CharField(max_length=200)),
                ('identifiant_national_affiliation', models.CharField(max_length=200)),
                ('type_identifiant_national_affiliation', models.CharField(max_length=200)),
                ('representants_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Info_generales')),
            ],
        ),
        migrations.CreateModel(
            name='Actions_menees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_menee', models.CharField(max_length=200)),
                ('action_menee_autre', models.CharField(max_length=200)),
                ('other1', models.CharField(max_length=200)),
                ('other2', models.CharField(max_length=200)),
                ('other3', models.CharField(max_length=200)),
                ('other4', models.CharField(max_length=200)),
                ('action_representation_interet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hatvp.Observations')),
            ],
        ),
    ]
