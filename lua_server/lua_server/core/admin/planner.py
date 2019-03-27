from django.contrib import admin
from ..models.planner import Planner, PlannerEntry


class PlannerInline(admin.StackedInline):
    model = Planner
    extra = 1


class PlannerEntryInline(admin.StackedInline):
    model = PlannerEntry
    extra = 1

@admin.register(Planner)
class PlannerAdmin(admin.ModelAdmin):
    inlines = [PlannerEntryInline]