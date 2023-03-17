from . import views
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostList.as_view(), name='post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='single_post'),
    path('account/signup/', views.register, name='account_register'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile', views.profile, name='profile'),
    path('account/password_reset/',
         auth_views.PasswordResetView.as_view(
            template_name='account/password_reset.html'),
         name="password_reset"),
    path('account/password_reset_done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='account/password_reset_done.html'),
         name="password_reset_done"),
    path('account/password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
          template_name='account/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path('account/password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
          template_name='account/password_reset_complete'),
         name="password_reset_complete"),
    path('subscribe', views.subscribe, name='subscribe')
]
