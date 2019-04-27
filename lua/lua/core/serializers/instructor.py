from rest_framework import serializers
from ..models.instructor import Instructor
from ..serializers.study_plan import StudyPlanSerializer


class InstructorSerializer(serializers.ModelSerializer):

    created_plans = StudyPlanSerializer(many=True)

    included_serializers = {
        'created_plans': StudyPlanSerializer
    }

    class Meta:
        model = Instructor
        fields = "__all__"
