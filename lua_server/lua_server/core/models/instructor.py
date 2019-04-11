from django.db import models
from .helpers.identifier import make_identifier
from .user import User
from .specialty import Specialty


class Instructor(User):
    bio = models.TextField(blank=True, max_length=500)
    specialty = models.ForeignKey(Specialty, related_name='instructors', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'user_instructors'
        ordering = ['-created_at']
        permissions = (
            ('can_create_plans', 'Can create student plans'),
        )

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
