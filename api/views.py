from rest_framework.views import APIView, Response
from api.serializers import UserSerializer, PostSerializer
from blog.models import Post


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
