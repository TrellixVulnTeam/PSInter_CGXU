from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from . import views
from .models import Warzywa
from rest_framework import status
from django.utils.http import urlencode
from django import urls


class WarzywaTests(APITestCase):
    def warzywa_category(self, name):
        url = reverse(views.WarzywoList.name)
        data = {'name': name}
        response = self.warzywa_category(url)
        return response
