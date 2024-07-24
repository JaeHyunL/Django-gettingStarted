from datetime import date
from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch

from .return_hello import hello
from .greet import *


# Create your tests here.
class DumyTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_dummy_test(self):
        self.assertEqual("hello", hello())


def fake_today():
    return date(2024, 7, 24)


class SampleTest(TestCase):
    @patch("inventory.greet.date", fake_today)
    def test_function_to_get_today(self):
        self.assertEqual("2024-07-24", function_to_get_today().strftime("%Y-%m-%d"))


class SimpleApiClientTest(TestCase):
    def test_run_greeting(self):
        client = APIClient()
        resp = client.get("inventory/greet/")
        self.assertEqual(resp.status_code, 200)
