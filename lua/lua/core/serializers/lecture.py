from rest_framework import serializers
from ..models.lecture import Lecture
from .helpers.choices import ChoicesSerializerField


class LectureSerializer(serializers.ModelSerializer):

    status = ChoicesSerializerField()

    class Meta:
        model = Lecture
        fields = "__all__"
