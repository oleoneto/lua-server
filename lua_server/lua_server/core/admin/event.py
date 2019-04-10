from django.contrib import admin
from ..models.event import Event


class EventInline(admin.StackedInline):
    model = Event
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']

    # Ensure current user is assigned as author of event instance.
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author_id = request.user.id
        obj.save()
