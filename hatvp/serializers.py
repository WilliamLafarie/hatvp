# serializers.py
from rest_framework import serializers

from .models import *


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Informations_generales
        fields = (
            'representants_id',
            'adresse',
            'code_postal',
            'derniere_publication_activite',
            'date_premiere_publication',
            'declaration_organisation_appartenance',
            'declaration_tiers',
            'denomination',
            'identifiant_national',
            'activites_publiees',
            'page_facebook',
            'page_linkedin',
            'page_twitter',
            'site_web',
            'nom_usage_HATVP',
            'pays',
            'sigle_HATVP',
            'type_identifiant_national',
            'ville',
            'label_categorie_organisation'
        )


class DirigeantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dirigeants
        fields = (
            'civilite_dirigeant',
            'fonction_dirigeant',
            'nom_dirigeant',
            'prenom_dirigeant',
            'representants_id',
            'nom_prenom_dirigeant'
        )

class CollaborateursSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaborateurs
        fields = (
            'civilite_collaborateur',
            'fonction_collaborateur',
            'nom_collaborateur',
            'prenom_collaborateur',
            'representants_id',
            'nom_prenom_collaborateur'
        )

class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = (
            'representants_id',
            'denomination_client',
            'identifiant_national_client',
            'type_identifiant_national_client',
        )

class AffiliationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Affiliations
        fields = (
            'representants_id',
            'denomination_affiliation',
            'identifiant_national_affiliation',
            'type_identifiant_national_affiliation',
        )

class Niveaux_interventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Niveaux_intervention
        fields = (
            'niveau_intervention',
            'representants_id',
        )

class ExercicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exercices
        fields = (
            'exercices_id',
            'representants_id',
            'date_debut',
            'date_fin',
            'exercice_sans_activite',
            'nombre_activite',
            'declaration_incomplete',
            'date_publication',
            'exercice_sans_CA',
            'montant_depense',
            'nombre_salaries',
            'chiffre_affaires',
            'annee_debut',
            'annee_fin',
            'montant_depense_inf',
            'montant_depense_sup',
            'ca_inf',
            'ca_sup',
        )

class Objets_activitesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objets_activites
        fields = (
            'activite_id',
            'exercices_id',
            'date_publication_activite',
            'identifiant_fiche',
            'objet_activite',
        )


class Domaines_interventionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domaines_intervention
        fields = (
            'domaines_intervention_actions_menees',
            'activite_id',
        )

class ObservationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Observations
        fields = (
            'action_representation_interet_id',
            'activite_id',
            'observation',
        )

class Decisions_concerneesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decisions_concernees
        fields = (
            'decision_concernee',
            'action_representation_interet_id',
        )

class BeneficiairesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beneficiaires
        fields = (
            'beneficiaire_action_menee',
            'action_representation_interet_id',
            'action_menee_en_propre',
        )

class Actions_meneesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actions_menees
        fields = (
            'action_menee',
            'action_representation_interet_id',
            'action_menee_autre',
        )

class Secteur_activitesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Secteur_activites
        fields = (
            'secteur_activite',
            'representants_id',
        )