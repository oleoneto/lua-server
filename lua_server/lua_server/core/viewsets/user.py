from rest_framework import viewsets
from ..models.user import User
from ..serializers.user import UserSerializer
from rest_framework import permissions
from .permissions.is_owner import IsAuthorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly)
