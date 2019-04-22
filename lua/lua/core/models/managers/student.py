# Remember to use the polymorphic to map models correctly
from django.db import models
from django.contrib.contenttypes.models import ContentType


class StudentManager(models.Manager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        queryset = super(StudentManager, self).filter(content_type=content_type, object_id=obj_id)
        return queryset
