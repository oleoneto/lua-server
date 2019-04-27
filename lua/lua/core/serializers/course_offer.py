from rest_framework import serializers
from ..models.course_offer import CourseOffer


class CourseOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseOffer
        fields = "__all__"
