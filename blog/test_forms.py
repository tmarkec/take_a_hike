from django.test import TestCase
from .forms import ProfileForm, FormUser
from django.contrib.auth.models import User


class UserForm(TestCase):

    def test_fields_are_explicit_in_form_metaclass(self):
        form = FormUser()
        self.assertEqual(
            form.Meta.fields,
            ('first_name', 'last_name', 'username', 'email', 'password1', 'password2'))


class ProfileFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password'
        )

    def test_profile_form(self):
        data = {
            'username': 'newusername',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'newemail@example.com',
        }
        form = ProfileForm(data=data, instance=self.user)
        self.assertTrue(form.is_valid())
        form.save()
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'newusername')
        self.assertEqual(self.user.first_name, 'John')
        self.assertEqual(self.user.last_name, 'Doe')
        self.assertEqual(self.user.email, 'newemail@example.com')