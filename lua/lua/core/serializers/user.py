from rest_framework import serializers
from ..models.user import User
from ..serializers.post import PostSerializer
from ..serializers.planner import PlannerSerializer


class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True)

    planners = PlannerSerializer()

    included_serializers = {
        'posts': PostSerializer,
        'planners': PlannerSerializer
    }

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'last_login',
                   'user_permissions', 'updated_at', 'date_joined')
