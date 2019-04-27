from rest_framework import serializers
from ..models.study_plan import StudyPlan
from ..models.learning_objective import LearningObjective


class StudyPlanSerializer(serializers.ModelSerializer):

    # learning_objectives = LearningObjectiveModuleSerializer(many=True)

    # included_serializers = {
    #     'modules': StudyModuleSerializer
    #     'learning_objectives': LearningObjectiveModuleSerializer
    # }

    class Meta:
        model = StudyPlan
        fields = "__all__"
