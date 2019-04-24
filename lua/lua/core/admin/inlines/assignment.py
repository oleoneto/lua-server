import nested_admin
from ...models.assignment import Assignment, Question, Answer, Option
from ...models.assignment import FileSubmission, AssignmentFile


class AssignmentInline(nested_admin.NestedStackedInline):
    model = Assignment
    extra = 0


class AssignmentFileInline(nested_admin.NestedStackedInline):
    model = AssignmentFile
    extra = 0


class FileSubmissionInline(nested_admin.NestedStackedInline):
    model = FileSubmission
    extra = 0


class OptionInline(nested_admin.NestedStackedInline):
    model = Option
    extra = 0


class QuestionInline(nested_admin.NestedStackedInline):
    model = Question
    inlines = [OptionInline]
    extra = 0


class AnswerInline(nested_admin.NestedStackedInline):
    model = Answer
    extra = 0
