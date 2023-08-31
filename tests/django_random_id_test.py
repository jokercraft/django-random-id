import unittest
from django.conf import settings

settings.configure()

settings.INSTALLED_APPS = (
    'myapp',
)

from src.django_random_id import generate_random_id


class TestDjangoRnadomID(unittest.TestCase):

    def test_generate_random_id(self):
        self.assertIsInstance(generate_random_id(), int)


unittest.main()
