from ..serializers.user import UserSerializer
from ..models.instructor import Instructor
from ..serializers.study_plan import StudyPlanSerializer


class InstructorSerializer(UserSerializer):

    created_plans = StudyPlanSerializer(many=True)

    included_serializers = {
        'created_plans': StudyPlanSerializer
    }

    class Meta(UserSerializer.Meta):
        model = Instructor
