from . import views
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .views import search_results


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.PostList.as_view(), name="post"),
    path("post/delete-comment/<int:comment_id>/",
         views.delete_comment, name="delete_comment"),
    path('comments/<int:comment_id>/update/',
         views.update_comment, name='update_comment'),
    path("search/", views.search_results, name="search_results"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="single_post"),
    path("like/<slug:slug>/", views.PostLike.as_view(), name="post_like"),
    path("account/signup/", views.register, name="account_register"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile", views.profile, name="profile"),
    path(
        "account/password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="account/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "account/password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="account/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "account/password_reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="account/password_reset_from_key.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "account/password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="account/password_reset_from_key_done.html"
        ),
        name="password_reset_complete",
    ),
    path("subscribe", views.subscribe, name="subscribe"),
]

handler404 = "take_a_hike.views.page_not_found_view"
