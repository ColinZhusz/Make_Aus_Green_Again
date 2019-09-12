from django.conf.urls import url
from django.urls import path, re_path
from MAGA import views
# from MAGA.models import ClassView

urlpatterns = [
    # index page
    url(r'^$', views.index, name='index'),

    url(r'^about/$', views.about, name='about'),

    # Education page
    url(r'^education/$', views.education, name='education'),

    # Information page
    url(r'^information/$', views.information, name='information'),

    # Classification
    url(r'^classification/$', views.classification, name='classification'),
    # path(r'^updateinfo/$', views.updateinfo,name='classification'),
    # path('', ClassView.as_view(), name='classification'),

    # Transformation
    url(r'^transformation/$', views.transformation, name='transformation'),

    # Calculator
    url(r'^calculator/$', views.calculator, name='calculator'),

    # upload photo
    # url(r'^classification/$', views.PicUpload.as_view(), name='classification'),

    # # show photo
    # re_path(r'^pic/upload/$',
    #         views.PicUpload.as_view(), name='pic_list'),
    #
    # re_path(r'^pic/(?P<pk>\d+)/$',
    #         views.PicDetail.as_view(), name='pic_detail'),
]
