from django.test import TestCase
from rest_framework import status
from django.utils import timezone


class ClientTestAPI(TestCase):

    def test_post_method(self):
        client = {
            "id": 1,
            "phone_number": "+79111277773",
            "code_provider": 1,
            "tag": "Москва",
            "timezone": "UTC"
        }
        response = self.client.post('http://127.0.0.1:8000/api/clients/', client)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_method(self):
        response = self.client.get('http://127.0.0.1:8000/api/clients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DistributionTestAPI(TestCase):

    def test_post_method(self):
        distribution = {
            "id": 39,
            "date_start": timezone.now(),
            "body": "tets",
            "date_finish": timezone.now(),
            "tag": "Москва",
            "code_provider": 1
        }
        response = self.client.post('http://127.0.0.1:8000/api/distributions/', distribution)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_method(self):
        response = self.client.get('http://127.0.0.1:8000/api/distributions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class StatisticTestAPI(TestCase):

    def test_get_method(self):
        response = self.client.get('http://127.0.0.1:8000/api/statistic/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
