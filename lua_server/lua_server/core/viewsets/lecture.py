from rest_framework import viewsets
from ..models.post import Lecture
from ..serializers.lecture import LectureSerializer


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.public()
    serializer_class = LectureSerializer
