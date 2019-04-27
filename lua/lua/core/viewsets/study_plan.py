from rest_framework import viewsets
from ..models.study_plan import StudyPlan
from ..serializers.study_plan import StudyPlanSerializer
from .permissions.is_member import IsMemberOrNoAccess


class StudyPlanViewSet(viewsets.ModelViewSet):
    queryset = StudyPlan.objects.all()
    serializer_class = StudyPlanSerializer
    permission_classes = [IsMemberOrNoAccess]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.id)
