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


def dashboard_home(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'SimpleExample', 'titlename': "Dashboard"})


def dashboard_informations(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'InformationsGenerales', 'titlename': "Informations générales"})


def dashboard_dirigeants(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Dirigeants', 'titlename': "Dirigeants"})


def dashboard_collaborateurs(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Collaborateurs', 'titlename': "Collaborateurs"})

def dashboard_clients(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Clients', 'titlename': "Clients"})


def dashboard_affiliations(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Affiliations', 'titlename': "Affiliations"})


def dashboard_niveaux_interventions(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'NiveauxInterventions', 'titlename': "Niveaux d'interventions"})


def dashboard_exercices(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Exercices', 'titlename': "Exercices"})


def dashboard_objets_activites(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'ObjetsActivites', 'titlename': "Objets activites"})


def dashboard_domaines_interventions(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'DomainesInterventions', 'titlename': "Domaines d'interventions"})

def dashboard_observations(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Observations', 'titlename': "Observations"})

def dashboard_decisions_conernees(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'DecisionsConcernees', 'titlename': "Decisions Concernees"})


def dashboard_beneficiaires(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Beneficiaires', 'titlename': "Bénéficiaires"})


def dashboard_actions_menees(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'ActionsMenees', 'titlename': "Actions Menées"})


def dashboard_secteur_activite(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'SecteurActivite', 'titlename': "Secteur d'activité"})


def dashboard_ministeres(request):
    return render(request, 'hatvp/dash.html', {'djangoApp': 'Ministeres', 'titlename': "Ministères"})
