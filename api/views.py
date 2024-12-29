from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.serializers import PostSerializer
from blog.models import Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    success_url = '/'
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'body']
    ordering_fields = ['created', 'updated', 'author']
    filterset_fields = ['author', 'created', 'updated']
