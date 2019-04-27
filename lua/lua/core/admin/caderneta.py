from django.contrib import admin
from ..models.caderneta import Caderneta


@admin.register(Caderneta)
class CadernetaAdmin(admin.ModelAdmin):
    pass
