from ..models.student import Student
from ..serializers.user import UserSerializer


class StudentSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        model = Student
