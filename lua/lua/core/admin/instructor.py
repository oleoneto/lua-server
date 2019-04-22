from django.contrib import admin
from ..models.instructor import Instructor
from .user import UserAdmin
from .study_plan import CreatedPlansInline
from .planner import PlannerInline


# @admin.register(Instructor)
class InstructorAdmin(UserAdmin):
    inlines = [PlannerInline, CreatedPlansInline]

