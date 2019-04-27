from rest_framework import viewsets
from rest_framework.response import Response
from .permissions.is_member import IsInCourseNoAccess
from ..models.enrollment import Enrollment
from ..serializers.enrollment import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsInCourseNoAccess]

    def list(self, request, *args, **kwargs):
        queryset = Enrollment.objects.filter(student__user=request.user)
        serializer = EnrollmentSerializer(queryset, many=True)
        return Response(serializer.data)
