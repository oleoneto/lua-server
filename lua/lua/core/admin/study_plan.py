from django.contrib import admin
from ..models.study_plan import StudyPlan, StudyModule, StudyModuleRequirement


class StudyModuleRequirementInline(admin.StackedInline):
    model = StudyModuleRequirement
    extra = 1


class StudyModuleInline(admin.StackedInline):
    model = StudyModule
    extra = 1

    # def has_add_permission(self, request, obj=None):
    #     return False
    #
    # def has_change_permission(self, request, obj=None):
    #     return False


@admin.register(StudyModule)
class StudyModuleAdmin(admin.ModelAdmin):
    pass


class CreatedPlansInline(admin.StackedInline):
    model = StudyPlan
    fk_name = 'creator'
    extra = 1
    readonly_fields = ('creator',)
    verbose_name = 'Plan you own'
    verbose_name_plural = 'Plans you own'


@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    inlines = [StudyModuleInline]

    readonly_fields = ['creator']

    list_display = ['id', 'title', 'creator', 'created_at', 'updated_at']

    # Ensure current user is assigned as author of plan instance.
    def save_model(self, request, obj, form, change):
        if request.user.has_perm('create_plan'):
            if not obj.creator_id:
                obj.creator_id = request.user.id
        obj.save()
