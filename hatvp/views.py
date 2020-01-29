from django.shortcuts import render


def index(request):
    return render(request, 'hatvp/index.html')


def lol(request):
    return render(request, 'hatvp/dash.html')
