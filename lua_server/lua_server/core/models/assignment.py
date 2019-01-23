from django.db import models
from lua_server.core.models.helpers.identifier import make_identifier
from .module import Module


class Assignment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    module = models.ForeignKey(Module, related_name='assignments', on_delete=models.DO_NOTHING)
    due_date = models.DateTimeField(blank=True)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'assignments'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
