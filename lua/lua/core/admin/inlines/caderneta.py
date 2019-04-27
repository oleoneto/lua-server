from django.contrib import admin
from ...models.caderneta import Caderneta


class CadernetaInline(admin.StackedInline):
    model = Caderneta
    extra = 1
