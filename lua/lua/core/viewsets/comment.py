from rest_framework import viewsets
from ..models.comment import Comment
from ..serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the comments
        for the currently authenticated user.
        """
        user = self.request.user
        return Comment.objects.filter(author=user)
