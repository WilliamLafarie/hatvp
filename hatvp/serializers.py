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
