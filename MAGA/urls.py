from django.conf.urls import url
from MAGA import views
urlpatterns = [
    #index page
    url(r'^$', views.index, name='home'),

	#Education page
    url(r'Education',views.edu,name = 'education'),

    #Information page
    url(r'Information',views.info, name ='information'),

    #Classification
    url(r'Classification', views.cla, name='classification'),


    #Transformation
    url(r'Transformation', views.trans, name='transformation'),

    #Calculator
    url(r'Calculator', views.calcu, name='calculator'),

]