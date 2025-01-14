from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mape', views.mape, name='mape')
    path('mape/add', views.dodaj_mapu, name='dodaj_mapu' )
]
