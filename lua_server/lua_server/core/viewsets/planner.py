from rest_framework import viewsets
from ..models.planner import Planner
from ..serializers.planner import PlannerSerializer


class PlannerViewSet(viewsets.ModelViewSet):
    queryset = Planner.objects.all()
    serializer_class = PlannerSerializer
