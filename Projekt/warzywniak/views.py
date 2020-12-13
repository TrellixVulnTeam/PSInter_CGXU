from django.http import HttpResponse
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Klienci, Warzywa, Zamowienia
from .serializers import KlienciSerializer, WarzywaSerializer, ZamowieniaSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User


class WarzywoList(generics.ListCreateAPIView):
    queryset = Warzywa.objects.all()
    serializer_class = WarzywaSerializer
    name = 'book-list'
    filter_fields = ['Warzywo', 'Cena']
    search_fields = ['Warzywo']
    ordering_fields = ['Warzywo', 'Cena']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class KlienciFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='PESEL', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='PESEL', lookup_expr='lte')

    class Meta:
        model = Klienci
        fields = ['from_birthdate','to_birthdate']


class KlienciList(generics.ListCreateAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    filter_class = KlienciFilter
    name = 'client-list'
    ordering_fields = ['Nazwisko', 'PESEL']


class ZamowieniaFilter(FilterSet):
    min_price = NumberFilter(field_name='Cena', lookup_expr='gte')
    max_price = NumberFilter(field_name='Cena', lookup_expr='lte')
    client_name = AllValuesFilter(field_name='Klienci__Nazwisko')

    class Meta:
        model = Zamowienia
        fields = ['min_price', 'max_price', 'client_name']


class ZamowieniaList(generics.ListCreateAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    filter_class = ZamowieniaFilter
    name = 'lista-zamowien'
