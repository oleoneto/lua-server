from django.contrib import admin
from ..models.study_plan import StudyPlan


class ManagedPlansInline(admin.StackedInline):
    model = StudyPlan
    fk_name = 'instructor'
    extra = 1
    verbose_name = 'Plan you manage'
    verbose_name_plural = 'Plans you manage'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CreatedPlansInline(admin.StackedInline):
    model = StudyPlan
    fk_name = 'creator'
    extra = 1
    readonly_fields = ('instructor',)
    verbose_name = 'Plan you own'
    verbose_name_plural = 'Plans you own'


@admin.register(StudyPlan)
class PlanAdmin(admin.ModelAdmin):
    readonly_fields = ['creator']

    # Ensure current user is assigned as author of plan instance.
    def save_model(self, request, obj, form, change):
        if request.user.has_perm('create_plan'):
            if not obj.creator_id:
                obj.creator_id = request.user.id
            if not obj.instructor_id:
                obj.instructor_id = request.user.id
        obj.save()
