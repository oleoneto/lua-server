from django.db import models
from .helpers.identifier import make_identifier
from .user import User
from .assignment import Assignment


class Assessment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(User, related_name='assessments', on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(Assignment, related_name='assessments', on_delete=models.DO_NOTHING)
    score = models.FloatField(blank=True)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'assessments'
        ordering = ['-created_at']
        unique_together = ('student', 'created_at')
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
