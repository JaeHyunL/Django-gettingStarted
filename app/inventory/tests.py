from django.test import TestCase
from return_hello import hello


# Create your tests here.
class DumyTestCase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_dummy_test(self):
        self.assertEqual("hello", hello())
