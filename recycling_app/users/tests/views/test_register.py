from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RegistrationTestCase(TestCase):
    def setUp(self):
        self.registration_url = reverse('register')
        self.username = 'testuser'
        self.password = 'Testpass1435!'
        self.email = 'test@example.com'

    def test_registration_form(self):

        response = self.client.get(self.registration_url)

        self.assertEqual(response.status_code, 200)


        self.assertContains(response, 'username')
        self.assertContains(response, 'password1')
        self.assertContains(response, 'password2')
        self.assertContains(response, 'email')

    def test_registration_process(self):

        response = self.client.post(self.registration_url, {
            'username': self.username,
            'password1': self.password,
            'password2': self.password,
            'email': self.email,
        })

        self.assertRedirects(response, reverse('login'))

        self.assertTrue(User.objects.filter(username=self.username).exists())

        user = User.objects.get(username=self.username)
        self.assertNotEqual(user.password, self.password)

