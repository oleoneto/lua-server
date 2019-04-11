from django.db import models
from .helpers.identifier import make_identifier
from .user import User


class Guest(User):
    # All guests must have a host, the user who has invited them to the service.
    host = models.ForeignKey(User, related_name='guests', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'user_guests'

    def __str__(self):
        return f'{self.username} - with {self.host.username}'
