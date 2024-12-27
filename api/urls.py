from django.urls import path
from api.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView

app_name = 'api'
urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='list'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='update'),
]
