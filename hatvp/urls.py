from django.urls import path
from hatvp.dash_apps import ptdr
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('lol/', views.lol, name="lol")
]


