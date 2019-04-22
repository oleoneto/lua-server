from django.contrib import admin
from ..models.role import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'users_in_role', 'updated_at']
