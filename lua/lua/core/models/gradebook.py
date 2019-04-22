from django.db import models
from .helpers.identifier import make_identifier
from .user import User
from .course import Course


class Gradebook(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(User, related_name='gradebooks', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, related_name='gradebooks', on_delete=models.DO_NOTHING)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'gradebooks'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'#{self.id}'
