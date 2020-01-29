from hatvp.dash_apps import simpleexample
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
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
