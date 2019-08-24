from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

appname = 'Make Australia Green Again'

def index(request):
<<<<<<< HEAD
    ...
    return redirect("http://18.221.149.227/MAGA/")

#
# def index(request):
#     context = {
#         'appname': appname,
#     }
#     return render(request, 'index.html', context)
=======
    context = {
        'appname': appname,
    }
    return render(request, 'index.html', context)
>>>>>>> d0e19170fbad1a5cdd4d1e4b6699f0286716c595


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
