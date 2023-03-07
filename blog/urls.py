from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostList.as_view(), name='post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='single_post'),
]
