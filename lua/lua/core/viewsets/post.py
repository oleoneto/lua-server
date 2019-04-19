from rest_framework import viewsets
from ..models.post import Post
from ..serializers.post import PostSerializer
from .permissions.is_owner import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
