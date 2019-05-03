from django.contrib import admin
from ..models.waitlist import Waitlist


@admin.register(Waitlist)
class WaitlistAdmin(admin.ModelAdmin):
    pass
