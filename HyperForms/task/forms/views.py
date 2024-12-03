from idlelib.sidebar import LineNumbers

from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'forms/index.html')
