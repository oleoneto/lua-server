from rest_framework import viewsets
from ..models.event import Event
from ..serializers.event import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
