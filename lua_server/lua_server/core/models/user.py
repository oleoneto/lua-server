from django.db import models
from cloudinary.models import CloudinaryField
from lua_server.core.models.helpers.identifier import make_identifier


class User(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    profile_picture = CloudinaryField('image')
    
    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'users'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at
