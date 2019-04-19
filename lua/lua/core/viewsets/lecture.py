from rest_framework import viewsets
from ..models.lecture import Lecture
from ..serializers.lecture import LectureSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
