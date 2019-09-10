from django.conf.urls import url
from django.views.generic.base import RedirectView
from MAGA import views

urlpatterns = [
    #index page
    url(r'^$', views.index, name='index'),

    url(r'^about/$',views.about,name = 'about'),

	#Education page
    url(r'^whyrecycle/$',views.whyrecycle,name = 'whyrecycle'),

    #Information page
    url(r'^council/$',views.council, name ='council'),

    #Classification
    url(r'^classification/$', views.classification, name='classification'),

    #Transformation
    url(r'^transformation/$', views.transformation, name='transformation'),

    #Calculator
    url(r'^calculator/$', views.calculator, name='calculator'),

    #Card Game
    url(r'^cardgame/$', views.cardgame, name='cardgame'),

    #favicon fix
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon/favicon.ico'),
)

]