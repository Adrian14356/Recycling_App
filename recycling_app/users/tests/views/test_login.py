from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials, email="testuser@wp.pl")

    def test_should_login_user_when_credentials_are_correct(self):
        response = self.client.post(reverse('login'), self.credentials, follow = True)
        self.assertTrue(response.context["user"].is_active)

    def test_should_reject_login_if_credentials_are_incorrect(self):
        response = self.client.post(reverse("login"), {"username" : "invaliduser", "password" : "invalidpassword"})
        self.assertTrue(response.status_code, 200)

    def test_should_redirect_user_after_correct_login_process(self):
        response = self.client.post(reverse('login'), self.credentials, follow=True)
        self.assertRedirects(response, reverse('home'))