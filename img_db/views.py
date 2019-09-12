from django.shortcuts import render

# Create your views here.
from img_db.models import IMG


def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/uploadimg.html')

def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name = request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'img_tem/uploadimg.html')