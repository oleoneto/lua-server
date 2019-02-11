from django.db import models
from .helpers.identifier import make_identifier
from .user import User


class Instructor(User):
    bio = models.TextField(blank=True, max_length=500)
    specialty = models.CharField(blank=True, max_length=100)
    
    class Meta:
        db_table = 'user_instructors'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
