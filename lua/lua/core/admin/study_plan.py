from django.contrib import admin
from ..models.study_plan import StudyPlan


class CreatedPlansInline(admin.StackedInline):
    model = StudyPlan
    fk_name = 'creator'
    extra = 1
    readonly_fields = ('creator',)
    verbose_name = 'Plan you own'
    verbose_name_plural = 'Plans you own'


@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    readonly_fields = ['creator']

    list_display = ['id', 'title', 'creator', 'created_at', 'updated_at']

    # Ensure current user is assigned as author of plan instance.
    def save_model(self, request, obj, form, change):
        if request.user.has_perm('create_plan'):
            if not obj.creator_id:
                obj.creator_id = request.user.teacher_profile.id
        obj.save()
