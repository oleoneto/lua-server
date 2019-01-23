from django.db import models
from .helpers.identifier import make_identifier
from .user import User


class Instructor(User):
    bio = models.TextField(blank=True, max_length=500)
    specialty = models.CharField(blank=True, max_length=100)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'user_instructors'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
