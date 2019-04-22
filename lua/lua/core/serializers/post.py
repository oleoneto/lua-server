from rest_framework_json_api import serializers
from ..models.post import Post
from .comment import CommentSerializer


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True)

    included_serializers = {
        'comments': CommentSerializer,
    }

    class Meta:
        model = Post
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['comments']
