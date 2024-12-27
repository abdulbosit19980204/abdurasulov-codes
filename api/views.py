from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import PostSerializer
from blog.models import Post
from .permissions import IsOwnerOrReadOnly


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    success_url = '/'
