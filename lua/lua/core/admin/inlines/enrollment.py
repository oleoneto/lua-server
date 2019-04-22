from django.contrib import admin
from ...models.enrollment import Enrollment


class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 0
