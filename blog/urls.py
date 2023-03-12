from . import views
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostList.as_view(), name='post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='single_post'),
    path('accounts/signup/', views.register, name='account_register'),
    path('profile/<int:user_id>/', views.profile, name='profile')
]
