from celery import shared_task
from . import views
from .models import Distribution, Client, Message
from notification.celery import app
from django.utils import timezone
import requests


@app.task(bind=True, retry_backoff=True)
def create_message(self,code,tag,pk):
    clients = Client.objects.filter(code_provider=code, tag=tag)
    try:
        new_message = Message.objects.create(
            distribution_id=pk,
        )
        new_message.client.set(clients)
        new_message.save()
    except requests.exceptions.RequestException as err:
        raise self.retry(exc=err)

