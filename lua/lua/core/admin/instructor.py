from django.contrib import admin
from ..models.instructor import Instructor
from .user import UserAdmin


# @admin.register(Instructor)
class InstructorAdmin(UserAdmin):
    pass

