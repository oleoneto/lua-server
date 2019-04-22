from django.contrib import admin
from .planner import PlannerInline
from ..models.student import Student
from .user import UserAdmin


# @admin.register(Student)
class StudentAdmin(UserAdmin):
    inlines = [PlannerInline]

    readonly_fields = ('student_id', 'internal_email',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email',
                       'password1', 'password2', 'photo', 'date_of_birth'),
        }),
    )

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name',
                       'date_of_birth', 'email', 'internal_email', 'student_id', 'password', 'photo')
        }),
        ('Permissions', {'fields': ('is_staff',)}),
    )
