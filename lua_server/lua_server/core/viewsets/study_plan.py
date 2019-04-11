from rest_framework import viewsets
from ..models.study_plan import StudyPlan
from ..serializers.study_plan import StudyPlanSerializer


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
