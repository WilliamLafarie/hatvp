from hatvp.dash_apps import simpleexample
from hatvp.dash_apps import informationsgenerales
from hatvp.dash_apps import collaborateurs
from hatvp.dash_apps import dirigeants
from hatvp.dash_apps import exercices
from hatvp.dash_apps import objetsactivites
from hatvp.dash_apps import niveauxinterventions
from hatvp.dash_apps import secteuractivite
from hatvp.dash_apps import observations
from hatvp.dash_apps import domainesinterventions
from hatvp.dash_apps import affiliations
from hatvp.dash_apps import clients
from hatvp.dash_apps import actionsmenees
from hatvp.dash_apps import decisionsconcernees
from hatvp.dash_apps import beneficiaires
from hatvp.dash_apps import ministeres
from django.urls import include, path
from rest_framework import routers
from . import views


# Register all the API's route

router = routers.DefaultRouter()
router.register(r'Informations_generales', views.InfoViewSet)
router.register(r'Dirigeants', views.DirigeantsViewSet)
router.register(r'Collaborateurs', views.CollaborateursViewSet)
router.register(r'Clients', views.ClientsViewSet)
router.register(r'Affiliations', views.AffiliationsViewSet)
router.register(r'Niveaux_intervention', views.Niveaux_interventionViewSet)
router.register(r'Exercices', views.ExercicesViewSet)
router.register(r'Objets_activites', views.Objets_activitesViewSet)
router.register(r'Domaines_intervention', views.Domaines_interventionViewSet)
router.register(r'Observations', views.ObservationsViewSet)
router.register(r'Decisions_concernees', views.Decisions_concerneesViewSet)
router.register(r'Beneficiaires', views.BeneficiairesViewSet)
router.register(r'Actions_menees', views.Actions_meneesViewSet)
router.register(r'Secteur_activites', views.Secteur_activitesViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/', views.dashboard_home, name="dashboard_home"),
    path('informations/', views.dashboard_informations, name="dashboard_informations"),
    path('dirigeants/', views.dashboard_dirigeants, name="dashboard_dirigeants"),
    path('collaborateurs/', views.dashboard_collaborateurs, name="dashboard_collaborateurs"),
    path('clients/', views.dashboard_clients, name="dashboard_clients"),
    path('affiliations/', views.dashboard_affiliations, name="dashboard_affiliations"),
    path('niveaux-interventions/', views.dashboard_niveaux_interventions, name="dashboard_niveaux_interventions"),
    path('exercices/', views.dashboard_exercices, name="dashboard_exercices"),
    path('objets-activites/', views.dashboard_objets_activites, name="dashboard_objets_activites"),
    path('domaines-interventions/', views.dashboard_domaines_interventions, name="dashboard_domaines_interventions"),
    path('observations/', views.dashboard_observations, name="dashboard_observations"),
    path('decisions-conernees/', views.dashboard_decisions_conernees, name="dashboard_decisions_conernees"),
    path('beneficiaires/', views.dashboard_beneficiaires, name="dashboard_beneficiaires"),
    path('actions-menees/', views.dashboard_actions_menees, name="dashboard_actions_menees"),
    path('secteur-activite/', views.dashboard_secteur_activite, name="dashboard_secteur_activite"),
    path('ministere/', views.dashboard_ministeres, name="dashboard_ministerex"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
