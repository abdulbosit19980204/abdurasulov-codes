from rest_framework.serializers import ModelSerializer
from blog.models import Post, Notification, VisitorsAddressModel
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.first_name
        token['username'] = user.username

        return token


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

    def create(self, validated_data):
        # Assign the currently authenticated user as the author
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)


class NotificationSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message']

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        notification = Notification.objects.create(**validated_data)
        return notification


class VisitorsAddressModelSerializer(ModelSerializer):
    class Meta:
        model = VisitorsAddressModel
        fields = '__all__'
    #
    # def create(self, validated_data):
    #     print(validated_data)
    #     address = VisitorsAddressModel.objects.create(**validated_data)
    #     return address
