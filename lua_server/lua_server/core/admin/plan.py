from django.contrib import admin
from ..models.plan import Plan


class ManagedPlansInline(admin.StackedInline):
    model = Plan
    fk_name = 'instructor'
    extra = 1


class CreatedPlansInline(admin.StackedInline):
    model = Plan
    fk_name = 'creator'
    extra = 1


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass
