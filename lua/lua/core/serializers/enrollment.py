from rest_framework import serializers
from ..models.enrollment import Enrollment
from .course import CourseSerializer
from .student import StudentSerializer


class EnrollmentSerializer(serializers.ModelSerializer):

    student = StudentSerializer()

    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['user', 'course']
