from rest_framework.serializers import ModelSerializer
from blog.models import Post
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created', 'updated']
        depth = 1
