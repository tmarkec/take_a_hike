from django.test import TestCase, Client
from django.urls import reverse
from .views import IndexView, PostDetail
from .models import User
from .forms import FormUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

