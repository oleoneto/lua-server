from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models.learning_objective import LearningObjective, LearningObjectiveFile, LearningOutcome, LearningLevel
from ..serializers.learning_objective import LearningObjectiveSerializer
from ..serializers.learning_objective import LearningObjectiveFileSerializer
from ..serializers.learning_objective import LearningOutcomeSerializer
from ..serializers.learning_objective import LearningLevelSerializer


class LearningObjectiveFileViewSet(viewsets.ModelViewSet):
    queryset = LearningObjectiveFile.objects.all()
    serializer_class = LearningObjectiveFileSerializer


class LearningObjectiveViewSet(viewsets.ModelViewSet):
    queryset = LearningObjective.objects.all()
    serializer_class = LearningObjectiveSerializer
    filter_fields = ['id', 'title', 'description']
    sort_fields = ['id', 'title', 'description', 'is_optional', 'created_at']
    filterset_fields = {
        'id': ('exact', 'lt', 'gt', 'gte', 'lte', 'in'),
        'title': ('icontains', 'iexact', 'contains'),
        'description': ('icontains', 'iexact', 'contains'),
    }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True)
    def files(self, request, pk=None):
        self.serializer_class = LearningObjectiveFileSerializer
        queryset = LearningObjectiveFile.objects.filter(learning_objective=self.get_object())
        serializer = LearningObjectiveFileSerializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def outcomes(self, request, pk=None):
        self.serializer_class = LearningOutcomeSerializer
        queryset = LearningOutcome.objects.filter(learning_objective=self.get_object())
        serializer = LearningOutcomeSerializer(queryset.distinct(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def levels(self, request, pk=None):
        self.serializer_class = LearningLevelSerializer
        queryset = LearningLevel.objects.filter(learning_objective=self.get_object())
        serializer = LearningLevelSerializer(queryset.distinct(), many=True)
        return Response(serializer.data)
