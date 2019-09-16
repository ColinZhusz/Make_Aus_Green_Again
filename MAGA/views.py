from django.shortcuts import render, HttpResponse

from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from MAGA.models import *

appname = 'Make Australia Green Again'


def index(request):
    context = {
        'appname': appname,
    }
    userCreate(request)
    return render(request, 'index.html', context)


def about(request):
    context = {
        'appname': appname,
    }
    return render(request, 'about.html', context)


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


def classification(request):
    if request.method == 'POST':
        ip = userIp(request)
        if detectUser(ip):
            u = User.objects.filter(ip_ad=ip).get()
            img = Uploaded_photo(photo_ad=request.FILES.get('img'), user=u)
        else:
            user = User(ip)
            user.save()
            img = Uploaded_photo(photo_ad=request.FILES.get('img'), user=user)
        img.save()
    context = {
        'appname': appname,
    }
    return render(request, 'classification.html', context)


def showImg(request):
    imgs = Uploaded_photo.objects.all()
    context = {
        'img': imgs
    }
    return render(request, 'showImg.html', context)


def userCreate(request):
    ip = userIp(request)
    if detectUser(ip):
        pass
    else:
        user = User(ip_ad=ip)
        user.save()


def detectUser(ip):
    if User.objects.filter(ip_ad=ip).exists():
        return True
    else:
        return False


def userIp(request):
    ip = request.META['REMOTE_ADDR']
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    return ip
