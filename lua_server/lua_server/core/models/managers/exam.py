# Remember to use the polymorphic to map models correctly
from django.db import models


class ExamQuerySet(models.QuerySet):
    def public(self):
        return self.exclude(is_private=True)

    def published(self):
        return self.filter(status='P')

    def liked(self):
        return self.filter(likes__gt=0)


class ExamManager(models.Manager):
    def get_queryset(self):
        return ExamQuerySet(self.model, using=self._db)
