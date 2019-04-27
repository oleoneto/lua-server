from django.contrib import admin
from ...models.course_offer import CourseOffer


class CourseOfferInline(admin.StackedInline):
    model = CourseOffer
    extra = 1
