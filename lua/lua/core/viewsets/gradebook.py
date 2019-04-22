from rest_framework import viewsets
from rest_framework.response import Response
from ..models.gradebook import Gradebook
from ..serializers.gradebook import GradebookSerializer
from .permissions.is_owner import IsStudentOrNoAccess


class GradebookViewSet(viewsets.ModelViewSet):
    queryset = Gradebook.objects.all()
    serializer_class = GradebookSerializer
    permission_classes = [IsStudentOrNoAccess]

    def list(self, request, *args, **kwargs):
        queryset = Gradebook.objects.filter(student=request.user)
        serializer = GradebookSerializer(queryset, many=True)
        return Response(serializer.data)
