from django.urls import path
from .views import PostApiView, PostEditApiView

urlpatterns = [
    path('posts/', PostApiView.as_view()),
    path('posts/<int:post_id>/', PostEditApiView.as_view())
]
