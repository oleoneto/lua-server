from django.db import models
from ..helpers.identifier import make_identifier
from ckeditor.fields import RichTextField


class BasePost(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_month=True, allow_unicode=True)
    content = RichTextField()
    is_draft = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    # Model managers
    objects = models.Manager

    class Meta:
        abstract = True
        ordering = ['-created_at']

    @property
    def has_likes(self):
        raise NotImplementedError

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'
