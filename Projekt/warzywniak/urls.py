from django.shortcuts import render
from django.urls import path
from polls.models import Question

from . import views
from .. import warzywniak

urlpatterns = [
    path('Warzywa', views.WarzywoList.as_view(), name=views.WarzywoList.name),
    path('Klienci', views.KlienciList.as_view(), name=views.KlienciList.name),
    path('Zamowienia', views.ZamowieniaList.as_view(), name=views.ZamowieniaList.name),
]