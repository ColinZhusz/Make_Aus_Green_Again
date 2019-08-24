from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

appname = 'Make Our Australia Green Again'

def index(request):
    context = {
        'appname': appname,
    }
    return render(request, 'index.html', context)


def education(request):
    context = {
        'appname': appname,
    }
    return render(request, 'education.html', context)

def information(request):
    context = {
        'appname': appname,
    }
    return render(request, 'information.html', context)


def classification(request):
    context = {
        'appname': appname,
    }
    return render(request, 'classification.html', context)

def transformation(request):
    context = {
        'appname': appname,
    }
    return render(request, 'transformation.html', context)

def calculator(request):
    context = {
        'appname': appname,
    }
    return render(request, 'calculator.html', context)
