from rest_framework import viewsets
from rest_framework import permissions
from ..models.caderneta import Caderneta
from ..serializers.caderneta import CadernetaSerializer


class CadernetaViewSet(viewsets.ModelViewSet):
    queryset = Caderneta.objects.all()
    serializer_class = CadernetaSerializer
