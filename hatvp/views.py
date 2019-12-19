from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InfoSerializer
from .models import Informations_generales


class InfoViewSet(viewsets.ModelViewSet):
    queryset = Informations_generales.objects.all().order_by('representants_id')
    serializer_class = InfoSerializer

def index(request):
    return render(request, 'hatvp/index.html')
