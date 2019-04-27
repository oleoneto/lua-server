from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models.post import Post
from ..models.comment import Comment
from ..models.user import User
from ..serializers.post import PostSerializer
from ..serializers.comment import CommentSerializer
from ..serializers.user import UserSerializer
from .permissions.is_owner import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.exclude(is_draft=True)
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_fields = ['id', 'title', 'content', 'comments']
    search_fields = ['id', 'title', 'content']
    filterset_fields = {
        'id': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'title': ('icontains', 'iexact', 'contains'),
        'content': ('icontains', 'iexact', 'contains'),
    }

    def list(self, request, *args, **kwargs):
        personal = Post.objects.filter(author=request.user)
        public = Post.objects.exclude(is_draft=True)
        queryset = personal or public
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    @action(detail=False)
    def liked(self, request):
        posts = self.queryset.filter(likes__username=request.user)

        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def comments(self, request, pk=None):
        comments = Comment.objects.filter(post=self.get_object())
        self.serializer_class = CommentSerializer
        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def author(self, request, pk=None):
        user = User.objects.get(id=self.get_object().author_id)
        self.serializer_class = UserSerializer
        serializer = self.get_serializer(user)
        return Response(serializer.data)
