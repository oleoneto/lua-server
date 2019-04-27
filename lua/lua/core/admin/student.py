from django.contrib import admin
from ..models.student import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'created_at', 'updated_at', 'is_active']
