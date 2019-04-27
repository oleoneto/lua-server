from rest_framework import viewsets
from rest_framework.response import Response
from ..models.gradebook import Gradebook
from ..serializers.gradebook import GradebookSerializer
from .permissions.is_member import IsInCourseNoAccess


class GradebookViewSet(viewsets.ModelViewSet):
    queryset = Gradebook.objects.all()
    serializer_class = GradebookSerializer
    permission_classes = [IsInCourseNoAccess]

    def list(self, request, *args, **kwargs):
        queryset = Gradebook.objects.filter(student__user=request.user)
        serializer = GradebookSerializer(queryset, many=True)
        return Response(serializer.data)
