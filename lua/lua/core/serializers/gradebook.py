from rest_framework import serializers
from ..models.gradebook import Gradebook
from .course import CourseSerializer
from .student import StudentSerializer


class GradebookSerializer(serializers.ModelSerializer):

    course = CourseSerializer()

    student = StudentSerializer()

    class Meta:
        model = Gradebook
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['course', 'student']
