from django.db import models
from .helpers.identifier import make_identifier
from .user import User


class Guest(User):
    # All guests must have a host, the user who has invited them to the service.
    host = models.ForeignKey(User, related_name='guests', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'user_guests'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.created_at
