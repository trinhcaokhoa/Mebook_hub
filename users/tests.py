from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SignUpPageView


class CustomUserTest(TestCase):
    def create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='trinh',
            email='caokhoa@yahoo.com',
            password='test123'
        )

        self.assertEqual(user.username, 'trinh')
        self.assertEqual(user.email, 'caokhoa@yahoo.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='cao',
            email='cao@yahoo.com',
            password='test123'
        )
        self.assertEqual(admin_user.username, 'cao')
        self.assertEqual(admin_user.email, 'cao@yahoo.com')
        self.assertTrue(admin_user.is_active)

        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
