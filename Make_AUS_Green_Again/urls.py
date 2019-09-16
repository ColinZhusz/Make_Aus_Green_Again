"""Make_AUS_Green_Again URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('MAGA.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# from django.conf.urls import url
# from django.views.static import serve
# from . import settings
# from django.conf.urls.static import static

# from MAGA import views

# urlpatterns = [
#     path('', include('MAGA.urls')),
#     # path('updateinfo/', views.updateinfo),
#     path('admin/', admin.site.urls),
#     url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})

# ]
