from rest_framework.serializers import ModelSerializer
from .models import CustomerUser
from rest_framework.fields import ReadOnlyField
from .models import Post



class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = ['email', 'username']


class PostSerializer(ModelSerializer):
    author_username = ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author_username', 'message']





