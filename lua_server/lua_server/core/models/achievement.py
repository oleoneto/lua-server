from django.db import models
from lua_server.core.models.helpers.identifier import make_identifier
from .badge import Badge
from .user import User


class Achievement(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    badge = models.ForeignKey(Badge, related_name='achievements', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name='achievements', on_delete=models.DO_NOTHING)
    date_acquired = models.DateTimeField(auto_now_add=True)
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'achievements'
        ordering = ['-created_at']
        unique_together = ('badge', 'user')
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
