from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('mape', views.mape, name='mape'),
    path('mape/add', views.addMap, name='addMap'),
    path('objekat/add', views.addObjekat, name='addObjekat'),
    path('objekat/<int:mapa_id>', views.objekti_mapa, name='objekti_mapa'),
]
