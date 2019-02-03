from rest_framework import serializers
import cloudinary
from ..models.user import User
from ..serializers.post import PostSerializer


class UserSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True)

    # TODO: Fix achievements relation

    profile_picture = serializers.SerializerMethodField()

    included_serializers = {
        'posts': PostSerializer,
    }

    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'is_staff', 'last_login', 'user_permissions', 'updated_at', 'date_joined')

    def get_profile_picture(self, obj):
        return cloudinary.CloudinaryImage(obj.profile_picture.public_id).build_url(secure=True)
