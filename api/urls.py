from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostListApiView.as_view(), name='list-posts'),
]
