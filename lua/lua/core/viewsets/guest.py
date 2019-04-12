from rest_framework import viewsets
from ..models.guest import Guest
from ..serializers.guest import GuestSerializer


class GuestViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
