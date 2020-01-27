from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Informations_generales', views.InfoViewSet)
router.register(r'Dirigeants', views.DirigeantsViewSet)
#router.register(r'Collaborateurs', views.InfoViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]