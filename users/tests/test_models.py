from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        user = get_user_model().objects.create_superuser(
            username='testuser',
            email='testuser@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class SignupTests(TestCase):
    username = 'newuser',
    email = 'newuser@email.com'

    def test_signup_page_works(self):

        response = self.client.get(reverse('account_signup'))
        no_response = self.client.get('/signup/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')
        self.assertContains(response, 'Sign Up')
        self.assertNotContains(response, 'Hi there! I should not be on this page.')
        self.assertEqual(no_response.status_code, 404)

    def test_signup_form(self):
        newuser = get_user_model().objects.create_user(
            username='newuser',
            email='newuser@email.com',
            password='newuser123'
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'newuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'newuser@email.com')
