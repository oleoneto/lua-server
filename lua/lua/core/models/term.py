from django.db import models


class Term(models.Model):
    """
    Default terms to be used to control course availability.
    """
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4
    TERM_CHOICES = (
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
    )

    id = models.PositiveSmallIntegerField(choices=TERM_CHOICES, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_terms'
        ordering = ['-created_at']

    def __str__(self):
        return self.get_id_display()
