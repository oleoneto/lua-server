from django.contrib import admin
from ..models.student import Student
from .planner import PlannerInline

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [PlannerInline]
