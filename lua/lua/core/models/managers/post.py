# Remember to use the polymorphic to map models correctly
from django.db import models


class PostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def public(self):
        return self.get_queryset().exclude(is_draft=True)

    def favorites(self):
        return self.get_queryset().annotate(num_likes=models.Count('likes')).filter(num_likes__gte=10)
