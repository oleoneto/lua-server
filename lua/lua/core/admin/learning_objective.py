from django.contrib import admin
from ..models.learning_objective import LearningObjective, LearningObjectiveFile, LearningOutcome


class LearningOutcomeInline(admin.StackedInline):
    model = LearningOutcome
    extra = 1


class LearningObjectiveFileInline(admin.StackedInline):
    model = LearningObjectiveFile
    extra = 1


@admin.register(LearningObjective)
class LearningObjectiveAdmin(admin.ModelAdmin):
    inlines = [LearningObjectiveFileInline, LearningOutcomeInline]
    list_display = ['id', 'title', 'total_files', 'grade_requirement', 'is_optional']
