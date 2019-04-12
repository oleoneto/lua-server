from rest_framework import viewsets
from ..models.post import Comment
from ..serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.public()
    serializer_class = CommentSerializer
