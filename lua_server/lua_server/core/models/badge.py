from django.db import models
from cloudinary.models import CloudinaryField
from lua_server.core.models.helpers.identifier import make_identifier


class Badge(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=30)
    level = models.IntegerField(blank=True)
    icon = CloudinaryField('image')
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'badges'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
