from django.db import models
from .helpers.identifier import make_identifier


class Specialty(models.Model):
    title = models.CharField(blank=True, max_length=30)
    level = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'user_specialties'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.created_at
