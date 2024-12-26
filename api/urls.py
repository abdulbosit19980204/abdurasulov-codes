from django.urls import path
from api.views import PostListView, PostListAPIView, PostCreateAPIView, PostListCreateAPIView, PostDetailAPIView, \
    PostDeleteAPIView, PostRetrieveUpdateDestroyAPIView

app_name = 'api'
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('apiview/', PostListAPIView.as_view(), name='list-apiview'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    path('plc/', PostListCreateAPIView.as_view(), name='list-create-apiview'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
    path('<int:pk>/update/', PostRetrieveUpdateDestroyAPIView.as_view(), name='update'),
]
