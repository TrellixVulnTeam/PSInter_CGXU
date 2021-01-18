from django.shortcuts import render
from django.urls import path
##from polls.models import Question

from . import views
#from .. import warzywniak

urlpatterns = [
    path('Warzywa', views.WarzywoList.as_view(), name=views.WarzywoList.name),
    path('Warzywa/<int:pk>', views.WarzywaDetail.as_view(), name=views.WarzywaDetail.name),
    path('Klienci', views.KlienciList.as_view(), name=views.KlienciList.name),
    path('Klienci/<int:pk>', views.KlienciDetail.as_view(), name=views.KlienciDetail.name),
    path('Zamowienia', views.ZamowieniaList.as_view(), name=views.ZamowieniaList.name),
    path('Zamowienia/<int:pk>', views.ZamowieniaDetail.as_view(), name=views.ZamowieniaDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]