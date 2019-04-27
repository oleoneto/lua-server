from django.contrib import admin
from ..models.enrollment import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    pass
