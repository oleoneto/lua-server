from rest_framework import viewsets
from rest_framework.decorators import action
from ..models.post import Post
from ..serializers.post import PostSerializer
from .permissions.is_owner import IsAuthorOrReadOnly
from .permissions.is_member import IsMemberOrNoAccess


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsMemberOrNoAccess]

    @action(detail=False)
    def liked(self, request):
        posts = Post.objects.filter(likes__username=request.user)

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

