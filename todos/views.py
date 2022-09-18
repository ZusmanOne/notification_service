from rest_framework import generics, viewsets
from rest_framework.response import Response
from .serializers import ClientSerializer, DistributionSerializer, MessageSerializer
from .models import Distribution, Client, Message
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from .tasks import create_message,send_message_openapi


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


class DistributionViewSet(viewsets.ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer

    @action(detail=True)
    def mailing_messages(self, request, pk=None):
        messages = Message.objects.filter(distribution=pk)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def general_statistic(request):
    """отображает общую статистику по созданным рассылкам и количеству
    отправленных сообщений по ним с группировкой по статусам"""
    distributions = Distribution.objects.all()
    general_statistic = {'Number of distribution': Distribution.objects.all().count()}
    info_messages = []
    for distribution in distributions:
        distribution_info = {'distribution': distribution.pk,
                             'messages': {
                                 'number of messages': distribution.message.all().count(),
                                 'sent': distribution.message.filter(status_send='SENT').count(),
                                 'not sent': distribution.message.filter(status_send='NOT SENT').count(),
                             }}
        info_messages.append(distribution_info)
    general_statistic['distribution statistics'] = info_messages
    return Response(general_statistic)


def send_message(distribution):
    now_time = timezone.now()
    if distribution.date_start < now_time < distribution.date_finish:
        create_message.apply_async((distribution.code_provider, distribution.tag, distribution.pk))
    if distribution.date_start >= now_time:
        create_message.apply_async((distribution.code_provider, distribution.tag, distribution.pk),
                                   eta=distribution.date_start, expires=distribution.date_finish)
    send_message_openapi.delay(distribution.pk)


@receiver(post_save, sender=Distribution)
def create_distribution(sender, instance, created, **kwargs):
    if created:
        send_message(instance)


