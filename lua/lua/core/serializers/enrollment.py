from rest_framework import serializers
from ..models.enrollment import Enrollment
from .course import CourseSerializer
from .user import UserSerializer


class EnrollmentSerializer(serializers.ModelSerializer):

    student = UserSerializer()

    course = CourseSerializer()

    class Meta:
        model = Enrollment
        fields = "__all__"

    class JSONAPIMeta:
        included_resources = ['user', 'course']
