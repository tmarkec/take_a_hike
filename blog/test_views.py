from django.test import TestCase, Client
from django.urls import reverse
from .views import IndexView, PostDetail, register, profile
from .models import User, Post, Comment, Subscription, Profile
from .forms import FormUser, SubcribersForm, UserForm, BioForm
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone


class TestViews(TestCase):
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('account_register')
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'john',
            'last_name': 'doe',
            'email': 'testuser@example.com',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        self.invalid_data = {
            'username': 'testuser',
            'email': 'invalidemail',
            'password1': 'testpass123',
            'password2': 'testpass456',
        }

    def test_register_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup-copy.html')
        self.assertIsInstance(response.context['form'], FormUser)

    def test_register_view_post_invalid_data(self):
        invalid_data = self.valid_data.copy()
        invalid_data['password2'] = 'wrongpass'
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup-copy.html')
        self.assertIsInstance(response.context['form'], FormUser)
        self.assertContains(response, "The two password fields didn’t match.")

    def test_register_view_post_valid_data(self):
        response = self.client.post(self.url, self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        user = User.objects.get(username=self.valid_data['username'])
        self.assertEqual(user.email, self.valid_data['email'])
        self.assertTrue(user.check_password(self.valid_data['password1']))
        self.assertTrue(user.is_authenticated)


# class PostDetailTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser', email='testuser@example.com',
#             password='testpassword')
#         self.post = Post.objects.create(
#             title='Test Post', slug='test-post', author=self.user,
#             content_header='Test content')
#         self.comment = Comment.objects.create(
#             post=self.post, name='Test User', email='testuser@example.com',
#             body='Test comment', approved=True)

#     def test_get_post_detail_page(self):
#         response = self.client.get(
#                    reverse('post_detail', kwargs={'slug': self.post.slug}))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'single_post.html')
#         self.assertContains(response, self.post.title)
#         self.assertContains(response, self.post.content_header)

class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
                    username='testuser', email='testuser@example.com',
                    password='testpassword')
        self.profile = Profile.objects.create(user=self.user, bio='Test bio')
    
    def test_profile_page(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile',
                                   kwargs={'user_id': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.profile.bio)

    def test_delete_profile(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('profile', kwargs={'user_id': self.user.id}), {'delete': 'delete'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertFalse(Profile.objects.filter(user=self.user).exists())