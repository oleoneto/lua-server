from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from ..models.user import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['id', 'username', 'name', 'is_staff']
    prepopulated_fields = {'username': ('first_name', 'last_name',)}
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password', 'photo')
        }),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'photo'),
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')
