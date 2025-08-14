from django.test import TestCase, Client
from django.urls import reverse
from .models import User  # Replace with your actual User model if custom

class AccountsModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")


class AccountsViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page_status_code(self):
        response = self.client.get(reverse("login"))  # Replace "login" with your URL name
        self.assertEqual(response.status_code, 200)

    def test_signup_page_status_code(self):
        response = self.client.get(reverse("signup"))  # Replace "signup" with your URL name
        self.assertEqual(response.status_code, 200)
