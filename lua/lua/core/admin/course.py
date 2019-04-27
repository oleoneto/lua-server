from django.contrib import admin
from ..models.course import Course
from .inlines.course_offer import CourseOfferInline


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseOfferInline]
    list_display = ['id', 'name', 'updated_at', 'is_being_taught']
