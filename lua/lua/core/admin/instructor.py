from django.contrib import admin
from ..models.instructor import Instructor


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'created_at', 'updated_at', 'is_active']
