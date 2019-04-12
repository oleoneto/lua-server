from rest_framework_json_api import serializers
from ..models.post import Post, PostLike
from .comment import CommentSerializer
from .lecture import LectureSerializer
from .helpers.choices import ChoicesSerializerField


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike


class PostSerializer(serializers.PolymorphicModelSerializer):
    
    polymorphic_serializers = [CommentSerializer, LectureSerializer]

    # TODO: Show status display name
    status = ChoicesSerializerField()

    likes_count = serializers.SerializerMethodField()

    included_serializers = {
        'comments': CommentSerializer,
        'likes': LikeSerializer,
    }

    class Meta:
        model = Post
        fields = "__all__"

    def get_likes_count(self, obj):
        return obj.likes.count()
