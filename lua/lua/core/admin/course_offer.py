from django.contrib import admin
from ..models.course_offer import CourseOffer
from .inlines.assignment import AssignmentInline


@admin.register(CourseOffer)
class CourseOfferAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]
    list_display = ['id', 'course', 'instructor', 'term', 'enrollment_limit', 'start_date']
