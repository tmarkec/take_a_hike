from django.test import TestCase
from django.utils import timezone
from .models import Subscription


class SubscriptionTestCase(TestCase):
    def test_subscription_creation(self):
        subscription = Subscription.objects.create(email='test@example.com')
        self.assertEqual(subscription.email, 'test@example.com')
        self.assertLessEqual(subscription.created_on, timezone.now())
        self.assertEqual(str(subscription), 'test@example.com')