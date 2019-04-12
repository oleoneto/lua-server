from rest_framework import serializers
from ..models.study_plan import StudyPlan, StudyModule, StudyModuleRequirement


class StudyModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudyModule
        fields = "__all__"


class StudyPlanSerializer(serializers.ModelSerializer):

    modules = StudyModuleSerializer(many=True)

    included_serializers = {
        'modules': StudyModuleSerializer
    }

    class Meta:
        model = StudyPlan
        fields = "__all__"
