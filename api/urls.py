from django.urls import path
from api.views import PostListView

app_name = 'api'
urlpatterns = [
    path('', PostListView.as_view(), name='list'),
]
