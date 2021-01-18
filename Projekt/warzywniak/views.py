from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Klienci, Warzywa, Zamowienia
from .serializers import KlienciSerializer, WarzywaSerializer, ZamowieniaSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class WarzywoList(generics.ListCreateAPIView):
    queryset = Warzywa.objects.all()
    serializer_class = WarzywaSerializer
    name = 'Lista Warzyw'
    filter_fields = ['Warzywo', 'Cena']
    search_fields = ['Warzywo']
    ordering_fields = ['Warzywo', 'Cena']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class KlienciFilter(FilterSet):
    from_birthdate = DateTimeFilter(field_name='PESEL', lookup_expr='gte')
    to_birthdate = DateTimeFilter(field_name='PESEL', lookup_expr='lte')

    class Meta:
        model = Klienci
        fields = ['from_birthdate', 'to_birthdate']


class KlienciList(generics.ListCreateAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    filter_class = KlienciFilter
    name = 'Lista Klientów'
    ordering_fields = ['Nazwisko', 'PESEL']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAdminUser]


class KlienciDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klienci.objects.all()
    serializer_class = KlienciSerializer
    name = 'klienci-detail'


class ZamowieniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    name = 'zamowienia-detail'


class WarzywaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warzywa.objects.all()
    serializer_class = WarzywaSerializer
    name = 'warzywa-detail'


class ZamowieniaFilter(FilterSet):
    min_price = NumberFilter(field_name='Cena', lookup_expr='gte')
    max_price = NumberFilter(field_name='Cena', lookup_expr='lte')

    class Meta:
        model = Zamowienia
        fields = ['min_price', 'max_price']


class ZamowieniaList(generics.ListCreateAPIView):
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    filter_class = ZamowieniaFilter
    name = 'Lista zamówień'
    permission_classes = [permissions.IsAuthenticated]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    def get(self, request, *args, **kwargs):
        return Response({'warzywa': reverse(WarzywoList.name, request=request),
                         'klienci': reverse(KlienciList.name, request=request),
                         'zamowienia': reverse(ZamowieniaList.name, request=request),
                         })
