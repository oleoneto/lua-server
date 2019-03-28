from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from .helpers.identifier import make_identifier
from .user import User


class Planner(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    user = models.ForeignKey(User, related_name='planners', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'user_planners'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}'


class PlannerEntry(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    planner = models.ForeignKey(Planner, related_name='entries', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=256)
    content = RichTextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'user_planner_entries'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - {self.title}'
