from django.db import models
from .helpers.identifier import make_identifier
from .user import User
from .specialty import Specialty


class Instructor(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    user = models.OneToOneField(User, related_name='teacher_profile', on_delete=models.DO_NOTHING)
    bio = models.TextField(blank=True, max_length=500)
    specialties = models.ManyToManyField(Specialty, related_name='instructors', blank=True)
    is_active = models.BooleanField(default=True, help_text='Activate or deactivate instructor account')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_user_instructors'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.name
