from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.PostList.as_view(), name='post')
]
