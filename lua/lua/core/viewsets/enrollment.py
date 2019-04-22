from rest_framework import viewsets
from rest_framework.response import Response
from .permissions.is_owner import IsStudentOrNoAccess
from ..models.enrollment import Enrollment
from ..serializers.enrollment import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsStudentOrNoAccess]

    def list(self, request, *args, **kwargs):
        queryset = Enrollment.objects.filter(student=request.user)
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(serializer.data)
