from rest_framework import viewsets
from rest_framework.response import Response
from ..models.assignment import Assignment
from ..models.student import Student
from ..models.instructor import Instructor
from ..serializers.assignment import AssignmentSerializer
from .permissions.is_member import IsInCourseNoAccess


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsInCourseNoAccess]
    filter_fields = ['id', 'name', 'description', 'files', 'due_date', 'points', 'questions']
    search_fields = ['name', 'description', 'due_date', 'points']
    filterset_fields = {
        'id': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'name': ('icontains', 'iexact', 'contains'),
        'description': ('icontains', 'iexact', 'contains'),
        'due_date': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'points': ('exact', 'lt', 'gt', 'gte', 'lte', 'in')
    }

    def list(self, request, *args, **kwargs):
        try:
            student = Student.objects.get(user=request.user)
            queryset = self.queryset.filter(course__offer_enrollments__student=student)
            queryset = self.filter_queryset(queryset)
            serializer = self.get_serializer(queryset.distinct(), many=True)
            return Response(serializer.data)
        except Student.DoesNotExist:
            try:
                instructor = Instructor.objects.get(user=request.user)
                queryset = self.queryset.filter(course_offer__instructor=instructor)
                queryset = self.filter_queryset(queryset)
                serializer = self.get_serializer(queryset.distinct(), many=True)
                return Response(serializer.data)
            except Instructor.DoesNotExist:
                return Response([])

