from django.contrib import admin
from ...models.gradebook import Gradebook


class GradebookInline(admin.StackedInline):
    model = Gradebook
    extra = 0
