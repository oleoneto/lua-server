from rest_framework import viewsets
from rest_framework import permissions
from ..models.course import Course
from ..serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
