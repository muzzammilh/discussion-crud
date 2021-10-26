from django.urls import path
from .views import PostApiView, PostSocialApiView

urlpatterns = [
    path('posts/', PostApiView.as_view()),
    path('posts/<int:post_id>/', PostApiView.as_view()),
    path('posts/like/<int:post_id>/', PostSocialApiView.as_view())
]
