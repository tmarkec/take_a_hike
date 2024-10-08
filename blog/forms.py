from .models import Comment, Subscription, Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm


class CommentForm(forms.ModelForm):
    """
    Form for creating comments
    """

    class Meta:
        model = Comment
        fields = ("body",)


class FormUser(UserCreationForm):
    """
    Form for creating new user account
    """

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        for field in ["username", "email", "password1", "password2"]:
            self.fields[field].help_text = None


class UserForm(UserChangeForm):
    """
    Form for updating user profile
    """

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in ["email", "password"]:
            self.fields[field].help_text = None


class BioForm(forms.ModelForm):
    """
    Form for updating user bio and profile image
    """
    image = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ["bio", "image"]


class SubcribersForm(forms.ModelForm):
    """
    Form for subscribing to a newsletter.
    """

    class Meta:
        model = Subscription
        fields = [
            "email",
        ]
