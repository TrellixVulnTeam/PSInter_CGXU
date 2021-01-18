from django.db import models
from djmoney.models.fields import *


class Klienci(models.Model):
    Imie = models.CharField(max_length=30)
    Nazwisko = models.CharField(max_length=30)
    PESEL = models.CharField(max_length=11, unique=True)
    Nr_Telefonu = models.CharField(max_length=12)


class Warzywa(models.Model):
    Warzywo = models.CharField(max_length=30)
    Cena = models.DecimalField(max_digits=8, decimal_places=2)


class Zamowienia(models.Model):
    id_warzywa = models.ForeignKey(Warzywa,related_name='zamowienia', on_delete=models.CASCADE)
    id_klienta = models.ForeignKey(Klienci,related_name='zamowienia', on_delete=models.CASCADE)
    Data_Zamowienia = models.DateTimeField(auto_now_add=False)
    Ilosc = models.IntegerField()

