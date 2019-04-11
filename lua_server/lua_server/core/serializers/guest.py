from rest_framework import serializers
from ..models.guest import Guest


class GuestSerializer(serializers.ModelSerializer):
    
    # Add related fields below:
    # Example relation fields are:
    # -- HyperlinkedIdentityField
    # -- HyperlinkedRelatedField
    # -- PrimaryKeyRelatedField
    # -- SlugRelatedField
    # -- StringRelatedField
    
    # You can also create a custom serializer, like so:
    # likes = LikeSerializer(many=True)

    class Meta:
        model = Guest
        fields = "__all__"
