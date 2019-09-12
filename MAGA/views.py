from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

appname = 'Make Australia Green Again'

def index(request):
    context = {
        'appname': appname,
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'appname': appname,
    }
    return render(request, 'about.html', context)

def whyrecycle(request):
    context = {
        'appname': appname,
    }
    return render(request, 'whyrecycle.html', context)

def council(request):
    context = {
        'appname': appname,
    }
    return render(request, 'council.html', context)


def classification(request):
    context = {
        'appname': appname,
    }
    return render(request, 'classification.html', context)

def facts(request):
    context = {
        'appname': appname,
    }
    return render(request, 'facts.html', context)

def calculator(request):
    context = {
        'appname': appname,
    }
    return render(request, 'calculator.html', context)

def cardgame(request):
    context = {
        'appname': appname,
    }
    return render(request, 'cardgame.html', context)
