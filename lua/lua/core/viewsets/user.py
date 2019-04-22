from rest_framework import viewsets
from ..models.user import User
from ..serializers.user import UserSerializer
from .permissions.is_owner import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_fields = ['username', 'first_name', 'last_name', 'email']
    search_fields = ['^username', '^first_name', '^last_name', '^email']
