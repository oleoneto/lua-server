from django.contrib import admin
from ...models.waitlist import Waitlist


class WaitlistInline(admin.StackedInline):
    model = Waitlist
    extra = 1
