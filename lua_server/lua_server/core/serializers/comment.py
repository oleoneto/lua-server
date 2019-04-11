from rest_framework import serializers
from ..models.post import Comment
from .helpers.choices import ChoicesSerializerField


class CommentSerializer(serializers.ModelSerializer):

    status = ChoicesSerializerField()

    class Meta:
        model = Comment
        fields = "__all__"