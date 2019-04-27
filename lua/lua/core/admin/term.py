from django.contrib import admin
from ..models.term import Term


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ['id']
