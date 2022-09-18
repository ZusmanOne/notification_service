from django.test import TestCase
from todos.models import Distribution, Client, Message
from django.utils import timezone


class DistributionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Distribution.object.create(
            date_start=timezone.now(),
            body='test text',
            date_finish=timezone.now(),
            tag='test tag',
            code_provider=1
        )

    def test_body_content(self):
        distribution = Distribution.objects.get(id=1)
        expected_object_name = f'{distribution.title}'
        self.assertEqual(expected_object_name, 'test text')

