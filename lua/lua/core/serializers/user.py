from rest_framework import serializers
from ..models.user import User
from ..serializers.post import PostSerializer
from ..serializers.planner import PlannerSerializer
from ..serializers.comment import CommentSerializer


class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True)

    planners = PlannerSerializer()

    comments = CommentSerializer(many=True)

    included_serializers = {
        'posts': PostSerializer,
        'planners': PlannerSerializer,
        'comments': CommentSerializer,
    }

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'last_login',
                   'user_permissions', 'updated_at', 'date_joined')

    class JSONAPIMeta:
        included_resources = ['posts', 'comments', 'planners']
