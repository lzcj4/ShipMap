from django.shortcuts import render


# Create your views here.

def index(request):
    context = {"gps": [120.015449, 30.2822]}
    return render(request, 'map/index.html', context)
