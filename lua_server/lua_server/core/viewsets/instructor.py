from rest_framework import viewsets
from ..models.instructor import Instructor
from ..serializers.instructor import InstructorSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
