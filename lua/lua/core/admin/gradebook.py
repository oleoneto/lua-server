from django.contrib import admin
from ..models.gradebook import Gradebook


# @admin.register(Gradebook)
class GradebookAdmin(admin.ModelAdmin):
    pass
