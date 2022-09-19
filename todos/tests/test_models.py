from django.test import TestCase
from todos.models import Distribution, Client, Message
from django.utils import timezone


class DistributionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.distribution = Distribution.objects.create(
            date_start=timezone.now(),
            body='test text',
            date_finish=timezone.now(),
            tag='test tag',
            code_provider=1
        )

    def test_instance_model(self):
        distribution = Distribution.objects.get(id=1)
        self.assertIsInstance(distribution, Distribution)

    def test_body_content(self):
        distribution = Distribution.objects.get(id=1)
        expected_object_name = f'{distribution.body}'
        self.assertEqual(expected_object_name, 'test text')

    def test_tag_content(self):
        distribution = Distribution.objects.get(id=1)
        expected_object_name = f'{distribution.tag}'
        self.assertEqual(expected_object_name, 'test tag')

    def test_code_provider_content(self):
        distribution = Distribution.objects.get(id=1)
        expected_object_name = distribution.code_provider
        self.assertEqual(expected_object_name, 1)


class ClientModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client.objects.create(
            phone_number="79876543211",
            code_provider=1,
            tag='test tag',
            timezone='UTC'

        )

    def test_instance_model(self):
        client = Client.objects.get(id=1)
        self.assertIsInstance(client, Client)

    def test_phone_number_content(self):
        client = Client.objects.get(id=1)
        expected_object_name = f'{client.phone_number}'
        self.assertEqual(expected_object_name, '79876543211')

    def test_code_provider_content(self):
        client = Client.objects.get(id=1)
        expected_object_name = client.code_provider
        self.assertEqual(expected_object_name, 1)

    def test_tag_content(self):
        client = Client.objects.get(id=1)
        expected_object_name = f'{client.tag}'
        self.assertEqual(expected_object_name, 'test tag')

    def test_timezone_content(self):
        client = Client.objects.get(id=1)
        expected_object_name = f'{client.timezone}'
        self.assertEqual(expected_object_name, 'UTC')


class MessageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.message = Message.objects.create(
            status_send='Not sent'
        )

    def it_can_be_attached_to_multiple_distributions(self):
        distributions = [Distribution.objects.create() for _ in range(3)]
        for distribution in distributions:
            distribution.message.add(self.message)

        self.assertEqual(len(distributions), self.message.distributions.count())
        for distribution in distributions:
            self.assertIn(distribution, self.message.distributions)

    def it_can_be_attached_to_multiple_client(self):
        clients = [Client.objects.create() for _ in range(3)]
        for client in clients:
            client.messages.add(self.client)

        self.assertEqual(len(clients), self.message.clients.count())
        for client in clients:
            self.assertIn(client, self.message.clients)
        self.assertIsInstance(self.message, Message)
