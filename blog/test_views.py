from django.test import TestCase, Client
from django.urls import reverse
from .views import IndexView, PostDetail
from .models import User, Post
from .forms import FormUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


class RegisterViewTestCase(TestCase):
    def test_register_success(self):
        # Submit a valid registration form
        response = self.client.post(reverse('account_register'), data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        
        # Check that the form was submitted successfully
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='testuser').exists())
        
        # Check that a success message was displayed
        messages = response.context.get('messages')
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your profile has been created')

    def test_register_failure(self):
        # Submit an invalid registration form (missing email)
        response = self.client.post(reverse('account_register'), data={
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        
        # Check that the form was not submitted successfully
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.exists())
        
        # Check that the form displayed an error message
        self.assertContains(response, 'This field is required.')