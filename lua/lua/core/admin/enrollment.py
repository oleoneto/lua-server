from django.contrib import admin
from ..models.enrollment import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'course', 'course_instructor']
