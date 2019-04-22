from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from ckeditor.fields import RichTextField
from .helpers.identifier import make_identifier
from .user import User


class Event(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)

    # `author_id` should be automatically set to the current user. Check implementation in `admin/event.py`
    owner = models.ForeignKey(User, related_name='events', on_delete=models.DO_NOTHING, editable=False)

    # Short title/description of the event. i.e "Student Appreciation Day"
    title = models.CharField(max_length=144, default="Event")

    # Date of the event (day, month, year)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')

    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')

    end_time = models.TimeField(u'Final time', help_text=u'Final time')

    # Some notes regarding the context and/or importance of the event
    notes = RichTextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    # Invite members to be part of this event
    participants = models.ManyToManyField(User, related_name='event_invitations', blank=True)

    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Calendar'

    @property
    def total_participants(self):
        return self.participants.count()

    # TODO: Clean this code
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False

        if new_start == fixed_end or new_end == fixed_start:
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end):
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end:
            overlap = True

        return overlap

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    yield ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}'
