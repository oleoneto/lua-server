from django.core.exceptions import ValidationError
from rest_framework import serializers
from ..models.event import Event
from .user import UserSerializer


class EventSerializer(serializers.ModelSerializer):

    participants = UserSerializer(many=True, allow_null=True)

    class Meta:
        model = Event
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['participants']

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        try:
            instance = Event.objects.create(**validated_data)
            for p in participants:
                instance.participants.add(p)
        except ValidationError as e:
            raise serializers.ValidationError(e.args[0])
        return instance

    def update(self, instance, validated_data):
        instance.save()
        return instance
