from rest_framework import viewsets
from rest_framework.response import Response
from ..models.event import Event
from ..serializers.event import EventSerializer
from .permissions.is_member import IsParticipantOrNoAccess


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsParticipantOrNoAccess]

    def list(self, request, *args, **kwargs):
        oqs = Event.objects.filter(owner=request.user)
        pqs = Event.objects.filter(participants__username=request.user)
        queryset = oqs | pqs
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

