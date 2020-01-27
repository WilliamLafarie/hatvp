from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


# Setting up all the view for each entity

class InfoViewSet(viewsets.ModelViewSet):
    queryset = Informations_generales.objects.all().order_by('representants_id')
    serializer_class = InfoSerializer


class DirigeantsViewSet(viewsets.ModelViewSet):
    queryset = Dirigeants.objects.all().order_by('representants_id')
    serializer_class = DirigeantsSerializer


class CollaborateursViewSet(viewsets.ModelViewSet):
    queryset = Collaborateurs.objects.all().order_by('representants_id')
    serializer_class = CollaborateursSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all().order_by('representants_id')
    serializer_class = ClientsSerializer


class AffiliationsViewSet(viewsets.ModelViewSet):
    queryset = Affiliations.objects.all().order_by('representants_id')
    serializer_class = AffiliationsSerializer


class Niveaux_interventionViewSet(viewsets.ModelViewSet):
    queryset = Niveaux_intervention.objects.all().order_by('representants_id')
    serializer_class = Niveaux_interventionSerializer


class ExercicesViewSet(viewsets.ModelViewSet):
    queryset = Exercices.objects.all().order_by('exercices_id')
    serializer_class = ExercicesSerializer


class Objets_activitesViewSet(viewsets.ModelViewSet):
    queryset = Objets_activites.objects.all().order_by('activite_id')
    serializer_class = Objets_activitesSerializer


class Domaines_interventionViewSet(viewsets.ModelViewSet):
    queryset = Domaines_intervention.objects.all().order_by('activite_id')
    serializer_class = Domaines_interventionSerializer


class ObservationsViewSet(viewsets.ModelViewSet):
    queryset = Observations.objects.all().order_by('action_representation_interet_id')
    serializer_class = ObservationsSerializer


class Decisions_concerneesViewSet(viewsets.ModelViewSet):
    queryset = Decisions_concernees.objects.all().order_by('action_representation_interet_id')
    serializer_class = Decisions_concerneesSerializer


class BeneficiairesViewSet(viewsets.ModelViewSet):
    queryset = Beneficiaires.objects.all().order_by('action_representation_interet_id')
    serializer_class = BeneficiairesSerializer


class Actions_meneesViewSet(viewsets.ModelViewSet):
    queryset = Actions_menees.objects.all().order_by('action_representation_interet_id')
    serializer_class = Actions_meneesSerializer


class Secteur_activitesViewSet(viewsets.ModelViewSet):
    queryset = Secteur_activites.objects.all().order_by('representants_id')
    serializer_class = Secteur_activitesSerializer


def index(request):
    return render(request, 'hatvp/index.html')
