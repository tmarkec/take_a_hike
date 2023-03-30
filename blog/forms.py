from .models import Comment, Subscription, Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


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
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        for field in ["username", "email", "password1", "password2"]:
            self.fields[field].help_text = None


class ProfileForm(UserChangeForm):
    """
    Form for updating user profile
    """

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in ["username", "email", "password"]:
            self.fields[field].help_text = None


class BioForm(UserChangeForm):
    """
    Form for updating user bio and profile image
    """

    class Meta:
        model = Profile
        fields = ["bio", "user_img"]


class SubcribersForm(forms.ModelForm):
    """
    Form for subscribing to a newsletter.
    """

    class Meta:
        model = Subscription
        fields = [
            "email",
        ]
