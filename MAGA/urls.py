from django.conf.urls import url
from MAGA import views
urlpatterns = [
    #index page
    url(r'^$', views.index, name='Make Our Australia Green Again'),
	#Education page
    url(r'Education',views.edu,name = 'edu page'),

    #Information page
    url(r'Information',views.info, name ='Information'),

    #Classification
    url(r'Classification', views.cla, name='Transformation'),


    #Transformation
    url(r'Transformation', views.trans, name='Transformation'),

]