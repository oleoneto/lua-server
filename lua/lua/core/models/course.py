from django.db import models
from .helpers.identifier import make_identifier
from django.utils import timezone


class Course(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True, max_length=700, help_text='What this course is about')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_courses'
        ordering = ['-created_at', 'name']

    @property
    def is_being_taught(self):
        offers = self.offers.filter(course=self)
        if offers:
            for offer in offers:
                if offer.end_date > timezone.now().date():
                    return True
        return False

    @property
    def is_available(self):
        # TODO: Implement is_available
        return False

    @property
    def available_in(self):
        # TODO: Implement available_in
        x = self.offers.filter(course=self).count()
        return f'{x} term(s)'

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
