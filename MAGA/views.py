from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from MAGA.models import Uploaded_photo
from . import models
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


# def classification(request):
#     context = {
#         'appname': appname,
#     }
#
#     return render(request, 'classification.html', {'img':img})




def classification(request):
    context = {
        'appname': appname,
    }
    return render(request, 'classification.html',context)

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

def uploadImg(request):
    if request.method == 'POST':
        img = Uploaded_photo(request.FILES.get('Uploaded_photo'))
        img.save()
    return render(request, 'classification.html',{'img':img})

#
# # Create show img views
# from django.views.generic import DetailView, ListView
# from django.views.generic.edit import CreateView
#
#
# class PicList(ListView):
#     queryset = Uploaded_photo.objects.all().order_by('-id')
#     context_object_name = 'latest_picture_list'
#
#
# class PicDetail(DetailView):
#     model = Uploaded_photo
#
#
# class PicUpload(CreateView):
#     model = Uploaded_photo
#     # fields = ['tag', 'image']
