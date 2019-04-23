from rest_framework import serializers
from ..models.user import User
from ..serializers.post import PostSerializer
from ..serializers.comment import CommentSerializer


class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, allow_null=True)

    comments = CommentSerializer(many=True, allow_null=True)

    included_serializers = {
        'posts': PostSerializer,
        'comments': CommentSerializer,
    }

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'last_login',
                   'user_permissions', 'updated_at', 'date_joined')

    class JSONAPIMeta:
        included_resources = ['posts', 'comments']
