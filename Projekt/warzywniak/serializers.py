import datetime

from rest_framework import serializers
from .models import Klienci, Warzywa, Zamowienia


class KlienciSerializer(serializers.ModelSerializer):
    zamowienia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienia-detail')
    class Meta:
        model = Klienci
        fields = ['url', 'pk', 'Imie', 'Nazwisko', 'PESEL', 'Nr_Telefonu','zamowienia']


class WarzywaSerializer(serializers.ModelSerializer):
    zamowienia = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienia-detail')
    class Meta:
        model = Warzywa
        fields = ['Warzywo', 'Cena','zamowienia']


class ZamowieniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zamowienia
        fields = ['id_klienta','id_warzywa','Data_Zamowienia', 'Ilosc']


