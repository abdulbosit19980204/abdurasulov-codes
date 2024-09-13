from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, UpdatePostView, PostDeleteView

app_name = 'posts'
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<int:pk>/post-update/', UpdatePostView.as_view(), name='update'),
    path('<int:pk>/post-delete/', PostDeleteView.as_view(), name='delete'),
    path('post-create/', PostCreateView.as_view(), name='create'),
]
