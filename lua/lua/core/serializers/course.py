from rest_framework import serializers
from ..models.course import Course
from .student import StudentSerializer


class CourseSerializer(serializers.ModelSerializer):

    included_serializers = {
        'students': StudentSerializer,
    }

    class Meta:
        model = Course
        fields = ('id',
                  'name',
                  'description',
                  'is_available')

    class JSONAPIMeta:
        included_resources = ['students']
