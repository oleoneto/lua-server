from django.contrib import admin
from ..models.course import Course
from .inlines.enrollment import EnrollmentInline
from .inlines.waitlist import WaitlistInline


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline, WaitlistInline]
    list_display = ['id', 'name', 'students_enrolled', 'waitlisted', 'updated_at', 'is_available']
