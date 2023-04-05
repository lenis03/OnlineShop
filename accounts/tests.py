from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import SESSION_KEY


class SignUpTest(TestCase):
    username = 'amir'
    email = 'amir@gmail.com'

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(user_model.objects.all().count(), 1)
        self.assertEqual(user_model.objects.all()[0].username, self.username)
        self.assertEqual(user_model.objects.all()[0].email, self.email)

    def test_signup_template_used(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'registration/signup.html')


class LogInTest(TestCase):
    def test_login_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_template_used(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')



