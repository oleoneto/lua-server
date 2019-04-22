from django.contrib import admin
from ..models.event import Event


class EventInline(admin.StackedInline):
    model = Event
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['owner', 'day', 'start_time', 'end_time', 'notes', 'total_participants']

    # Ensure current user is assigned as author of event instance.
    def save_model(self, request, obj, form, change):
        if not obj.owner_id:
            obj.owner_id = request.user.id
        obj.save()
