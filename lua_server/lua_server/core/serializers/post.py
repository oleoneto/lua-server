from rest_framework_json_api import serializers
from ..models.post import Post, Comment, Lecture


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        resource_name = 'Comment'
        model = Comment
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        resource_name = 'Lecture'
        model = Lecture
        fields = '__all__'


class PostSerializer(serializers.PolymorphicModelSerializer):
    
    polymorphic_serializers = [CommentSerializer, LectureSerializer]

    # TODO: Show status display name
    status = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_status(self, obj):
        return obj.get_status_display()
