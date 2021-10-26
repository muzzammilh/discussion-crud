from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    user_likes_data = UserSerializer(source='user_likes', many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'user', 'body', 'likes', 'created_at', 'user_likes_data']