from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Informations_generales.objects.all().order_by('representants_id')
    serializer_class = InfoSerializer


class DirigeantsViewSet(viewsets.ModelViewSet):
    queryset = Dirigeants.objects.all().order_by('representants_id')
    serializer_class = DirigeantsSerializer


def index(request):
    return render(request, 'hatvp/index.html')
