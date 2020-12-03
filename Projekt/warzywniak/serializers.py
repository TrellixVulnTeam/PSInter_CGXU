from rest_framework import serializers
from .models import Klienci, Warzywa, Zamowienia


class KlienciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klienci
        fields = ['id', 'Imie', 'Nazwisko', 'PESEL', 'Nr_Telefonu']


class WarzywaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warzywa
        fields = ['id', 'Warzywo', 'Cena']


class ZamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienia
        fields = ['id', 'id_Warzywa', 'id_Klienta', 'Data_Zamowienia', 'Ilosc']
    #def SprawdzenieDaty(self, Data_Zamowienia):
