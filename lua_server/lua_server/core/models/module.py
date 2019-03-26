from django.db import models
from .helpers.identifier import make_identifier
from .plan import Plan


class Module(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    plan = models.ForeignKey(Plan, related_name='modules', on_delete=models.DO_NOTHING)
    is_required = models.BooleanField(default=True)

    name = models.CharField(max_length=256)
    subject = models.CharField(max_length=100)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'learning_modules'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.name}"
