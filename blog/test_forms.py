from django.test import TestCase
from .forms import UserForm, FormUser
from django.contrib.auth.models import User


class FormUserTestCase(TestCase):
    def test_form_user_missing_data(self):
        form = FormUser(
            {
                "username": "",
                "first_name": "",
                "last_name": "",
                "email": "",
                "password1": "",
                "password2": "",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], ["This field is required."])
        self.assertEqual(form.errors["first_name"],
                         ["This field is required."])
        self.assertEqual(form.errors["last_name"], ["This field is required."])
        self.assertEqual(form.errors["email"], ["This field is required."])
        self.assertEqual(form.errors["password1"], ["This field is required."])
        self.assertEqual(form.errors["password2"], ["This field is required."])

    def test_form_user_help_text(self):
        form = FormUser()
        self.assertEqual(form.fields["username"].help_text, None)
        self.assertEqual(form.fields["email"].help_text, None)
        self.assertEqual(form.fields["password1"].help_text, None)
        self.assertEqual(form.fields["password2"].help_text, None)


class UserFormTestCase(TestCase):
    def test_user_form_valid(self):
        form_data = {'first_name': 'John',
                     'last_name': 'Doe', 'email': 'johndoe@example.com'}
        form = UserForm(data=form_data)
        assert form.is_valid() == True

    def test_user_form_invalid_email(self):
        form_data = {'first_name': 'John',
                     'last_name': 'Doe', 'email': 'johndoexample.com'}
        form = UserForm(data=form_data)
        assert form.is_valid() == False

    def test_form_user_help_text(self):
        form = UserForm()
        self.assertEqual(form.fields["email"].help_text, None)
        self.assertEqual(form.fields["password"].help_text, None)
