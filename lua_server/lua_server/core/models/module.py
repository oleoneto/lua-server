from django.db import models
from .helpers.identifier import make_identifier
from .course import Course


class Module(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.DO_NOTHING)
    subject = models.CharField(max_length=100)
    is_required = models.BooleanField(default=True)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'modules'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
