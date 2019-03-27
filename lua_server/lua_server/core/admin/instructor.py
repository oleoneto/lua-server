from django.contrib import admin
from ..models.plan import Plan
from ..models.planner import Planner, PlannerEntry
from ..models.instructor import Instructor
from .user import UserAdmin
from .plan import CreatedPlansInline, ManagedPlansInline
from .planner import PlannerInline, PlannerEntryInline


@admin.register(Instructor)
class InstructorAdmin(UserAdmin):
    inlines = [PlannerInline, ManagedPlansInline]
