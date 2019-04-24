from django.contrib import admin
import nested_admin
from ..models.assignment import Assignment, AssignmentType, Question
from .inlines.assignment import AssignmentInline, AssignmentFileInline, QuestionInline, OptionInline


@admin.register(Assignment)
class AssignmentAdmin(nested_admin.NestedModelAdmin):
    inlines = [AssignmentFileInline, QuestionInline]
    list_display = ['name', 'course', 'public', 'total_questions', 'total_files', 'total_file_submissions']


@admin.register(AssignmentType)
class AssignmentTypeAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]
    list_display = ['id', 'assignment_count']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
