from django.shortcuts import render
from rest_framework import generics
from .serializers import ClientSerializer, DistributionSerializer
from .models import  Distribution, Client, Message


class ClienList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class DistributionList(generics.ListCreateAPIView):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer


class DistributionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer


# Create your views here.
