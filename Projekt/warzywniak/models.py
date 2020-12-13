from django.db import models
from djmoney.models.fields import MoneyField

class Klienci(models.Model):
    Imie = models.CharField(max_length=30)
    Nazwisko = models.CharField(max_length=30)
    PESEL = models.CharField(max_length=11, unique=True)
    Nr_Telefonu = models.CharField(max_length=12)


class Warzywa(models.Model):
    Warzywo = models.CharField(max_length=30)
    Cena = MoneyField(max_digits=8, decimal_places=2, default_currency='PLN')


class Zamowienia(models.Model):
    id_Warzywa = models.ForeignKey(Warzywa, on_delete=models.CASCADE)
    id_Klienta = models.ForeignKey(Klienci, on_delete=models.CASCADE)
    Data_Zamowienia = models.DateTimeField(auto_now_add=True)
    Ilosc = models.IntegerField()

