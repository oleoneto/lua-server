from rest_framework import viewsets
from ..models.course_offer import CourseOffer
from ..serializers.course_offer import CourseOfferSerializer


class CourseOfferViewSet(viewsets.ModelViewSet):
    queryset = CourseOffer.objects.all()
    serializer_class = CourseOfferSerializer
