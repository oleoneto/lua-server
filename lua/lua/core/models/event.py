from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse
from ckeditor.fields import RichTextField
from .helpers.identifier import make_identifier
from .helpers.mailer import send_mail
from .user import User


DEFAULT_INVITATION_SUBJECT = """Lua: An invite from {}"""

DEFAULT_INVITATION = """
Hello {},

{} would like to share the following event with you:

Title: {} 
on {} at {} - {}

Sincerely,
Admin Team @ Lua LMS
"""


class Event(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)

    # `author_id` should be automatically set to the current user. Check implementation in `admin/event.py`
    owner = models.ForeignKey(User, related_name='events', on_delete=models.PROTECT, editable=False)

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
        db_table = 'core_events'
        ordering = ['day', 'start_time', 'title']

    @property
    def total_participants(self):
        return self.participants.count()

    def notify_new_participant(self, participant=None):
        try:
            send_mail(user=participant, subject=DEFAULT_INVITATION_SUBJECT.format(self.owner.name),
                      message=DEFAULT_INVITATION.format(participant.name, self.owner.name,
                                                        self.title, self.day,
                                                        self.start_time, self.end_time))

            print(f'Email sent to {participant.name} - {participant.email}')
        except NameError:
            return

    def overlaps(self, query_instance):
        """
        Current event: self
        Queryset event: Q
        """
        # Takes place within another event timeline
        # Starts in the past (before q.start) but overlaps at the end
        # Starts in the future (after q.start) but overlaps at the end
        # Starts in the future (after q.start) but stays inside event
        if query_instance.start_time <= self.start_time <= query_instance.end_time or \
                query_instance.start_time <= self.end_time <= query_instance.end_time or \
                query_instance.start_time <= self.start_time >= query_instance.end_time:
            return True

        return False

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def is_same_event(self, event):
        if (self.title == event.title) and \
                (self.day == event.day) and \
                (self.start_time == event.start_time):
            return True
        return False

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Please make sure ending times are after starting times')

        events = Event.objects.filter(day=self.day).exclude(id=self.id).filter(owner=self.owner_id)
        if events.exists():
            for event in events:
                if self.is_same_event(event=event):
                    raise ValidationError('Event already exists')
                if self.overlaps(query_instance=event):
                    raise ValidationError(
                        f'There is an overlap with another event: {event.title} on {event.day}, between {event.start_time} and {event.end_time}')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        self.clean()

        # TODO: Fix self-invitations
        # if self.owner in self.participants:
        #     self.participants = self.participants.exclude(username=self.owner.username)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}'
