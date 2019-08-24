from django.conf.urls import url
from MAGA import views
urlpatterns = [
    #index page
    url(r'^$', views.index, name='index'),

	#Education page
    url(r'^education/$',views.education,name = 'education'),

    #Information page
    url(r'^information/$',views.information, name ='information'),

    #Classification
    url(r'^classification/$', views.classification, name='classification'),

    #Transformation
    url(r'^transformation/$', views.transformation, name='transformation'),

    #Calculator
    url(r'^calculator/$', views.calculator, name='calculator'),

]