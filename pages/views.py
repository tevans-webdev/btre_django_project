from django.shortcuts import render
from django.http import HttpResponse


def indexPage(request):
    return render(request, 'pages/index.html')


def aboutPage(request):
    return render(request, 'pages/about.html')
