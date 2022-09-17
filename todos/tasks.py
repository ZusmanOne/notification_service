from celery import shared_task
from . import views
from .models import Distribution, Client, Message
from notification.celery import app
from django.utils import timezone


@app.task
def create_message(code,tag,pk):
    clients = Client.objects.filter(code_provider=code, tag=tag)
    new_message = Message.objects.create(
        distribution_id=pk,
    )
    new_message.client.set(clients)
    new_message.save()

