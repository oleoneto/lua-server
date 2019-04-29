from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models.caderneta import Caderneta
from ..serializers.caderneta import CadernetaSerializer
from ..serializers.user import UserSerializer
from ..serializers.study_plan import StudyPlanSerializer
from ..serializers.learning_objective import LearningObjectiveSerializer, LearningObjective
from .permissions.is_member import IsMemberOrNoAccess


class CadernetaViewSet(viewsets.ModelViewSet):
    queryset = Caderneta.objects.all()
    serializer_class = CadernetaSerializer
    permission_classes = [IsMemberOrNoAccess]

    def list(self, request, *args, **kwargs):
        queryset = Caderneta.objects.filter(student__user=request.user)
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def student(self, request, pk=None):
        instance = self.get_object()
        who = instance.student.user
        self.serializer_class = UserSerializer
        serializer = self.get_serializer(who)
        return Response(serializer.data)

    @action(detail=True)
    def plan(self, request, pk=None):
        instance = self.get_object()
        study_plan = instance.study_plan
        self.serializer_class = StudyPlanSerializer
        serializer = self.get_serializer(study_plan)
        return Response(serializer.data)

    @action(detail=True)
    def objectives(self, request, pk=None):
        instance = self.get_object()
        objectives = LearningObjective.objects.filter(study_plans__cadernetas=instance)
        self.serializer_class = LearningObjectiveSerializer

        page = self.paginate_queryset(objectives)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(objectives, many=True)
        return Response(serializer.data)
