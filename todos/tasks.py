from .models import Distribution, Client, Message
from notification.celery import app
import requests
from urllib.parse import urljoin
from environs import Env

env = Env()
env.read_env()


TOKEN = env('TOKEN')
url = 'https://probe.fbrq.cloud/v1/send/'


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


@app.task(bind=True, retry_backoff=True)
def send_message_openapi(self, distribution_pk):
    distribution = Distribution.objects.get(pk=distribution_pk)
    distribution_messages = distribution.message.all()
    data={}
    for mailing in distribution_messages:
        for client in mailing.client.all():
            data['id']=mailing.pk
            data['phone'] = client.phone_number_e164
            data['text'] = distribution.body
    url_page = urljoin(url, str(data['id']))
    headers = {
        'Authorization': f"Bearer {TOKEN}",
        'Content-Type': 'application/json',
    }
    response = requests.post(url_page, headers=headers, json=data)
    response.raise_for_status()

