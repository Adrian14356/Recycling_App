from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

client = Client()

class TestRegister(TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_should_return_200_when_user_send_request(self):
        resp = client.get(reverse('register'))
        code = resp.status_code
        expected_code = 200
        self.assertEquals(code, expected_code)

# sprawdzic czy użytkoniwk dodaje sie do bazy danych 