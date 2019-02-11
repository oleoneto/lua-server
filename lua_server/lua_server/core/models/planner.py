from django.db import models
from cloudinary.models import CloudinaryField
from .helpers.identifier import make_identifier
from .instructor import Instructor


class Planner(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    instructor = models.ForeignKey(Instructor, related_name='planners', on_delete=models.DO_NOTHING)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'instructor_planners'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
