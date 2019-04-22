from rest_framework import serializers
from ..models.gradebook import Gradebook
from .course import CourseSerializer
from .user import UserSerializer


class GradebookSerializer(serializers.ModelSerializer):

    course = CourseSerializer()

    student = UserSerializer()

    class Meta:
        model = Gradebook
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['course', 'student']
