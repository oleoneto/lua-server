from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from ..models.event import Event
from ..serializers.event import EventSerializer
from .user import User
from .permissions.is_member import IsParticipantOrNoAccess
from .permissions.is_owner import IsOwnerOrNoAccess


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsParticipantOrNoAccess]
    filter_fields = ['title', 'notes', 'owner', 'participants']
    search_fields = ['title', 'notes', 'id']
    filterset_fields = {
        'id': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'title': ('icontains', 'iexact', 'contains'),
        'notes': ('icontains', 'iexact', 'contains'),
    }

    def list(self, request, *args, **kwargs):
        oqs = Event.objects.filter(owner=request.user)
        pqs = Event.objects.filter(participants__username=request.user)
        queryset = oqs | pqs
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['patch'], permission_classes=[IsOwnerOrNoAccess])
    def invite(self, request, pk=None):
        print('Begin invite')
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            participants = request.data.get('participants')
            notify_list = []

            if participants:
                for p in participants:
                    try:
                        user = User.objects.get(id=p.get('id'))
                        try:
                            user.event_invitations.get(id=instance.id)
                        except Event.DoesNotExist:
                            instance.participants.add(user)
                            print(f"Add {user.name} to {instance.title}")
                            notify_list.append(user)
                    except User.DoesNotExist:
                        pass

            self.perform_update(serializer=serializer)

            # TODO: Handle email notifications
            if notify_list:
                for user in notify_list:
                    self.notify_participant(instance=instance, participant=user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def notify_participant(self, instance, participant=None):
        instance.notify_new_participant(participant=participant)
