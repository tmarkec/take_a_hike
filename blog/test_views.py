from django.test import TestCase, Client
from django.urls import reverse
from .views import IndexView, PostDetail
from .models import User, Post
from .forms import FormUser, SubcribersForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.core.mail import outbox


class TestViews(TestCase):
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class PostDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            content='This is a test post',
            status=1
        )

    def test_post_detail_view(self):
        url = reverse('post_detail', args=[self.post.slug])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'single_post.html')
        self.assertEqual(response.context['post'], self.post)
        self.assertQuerysetEqual(
            response.context['comments'],
            self.post.comments.filter(approved=True).order_by('-created_on'),
            transform=lambda x: x
        )
        self.assertFalse(response.context['commented'])
        self.assertFalse(response.context['liked'])
        self.assertIsInstance(response.context['comment_form'], CommentForm)