<<<<<<< HEAD
from django.urls import path
from hatvp.dash_apps import ptdr
=======
from django.urls import include, path
from rest_framework import routers
>>>>>>> ec7a6ffe673cf6c445e8e12de95b41e096faf68d
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
<<<<<<< HEAD
    path('lol/', views.lol, name="lol")
]


=======
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
>>>>>>> ec7a6ffe673cf6c445e8e12de95b41e096faf68d
