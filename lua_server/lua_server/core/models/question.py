from django.db import models
from .helpers.identifier import make_identifier
from .assignment import Assignment


class Question(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    assignment = models.ForeignKey(Assignment, related_name='questions', on_delete=models.DO_NOTHING)
    content = models.TextField()
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'questions'
        ordering = ['-created_at']
        unique_together = ('id', 'assignment')
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
