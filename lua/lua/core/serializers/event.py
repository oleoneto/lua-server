from rest_framework import serializers
from ..models.event import Event
from .user import UserSerializer


class EventSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True)

    class Meta:
        model = Event
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['participants']
