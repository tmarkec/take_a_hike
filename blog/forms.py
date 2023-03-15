from .models import Comment, Subscription
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class FormUser(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(FormUser, self).__init__(*args, **kwargs)
        for field in ['username', 'email', 'password1', 'password2']:
            self.fields[field].help_text = None


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in ['username', 'email',]:
            self.fields[field].help_text = None


class SubcribersForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email',]