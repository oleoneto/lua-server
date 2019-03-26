from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gl_
from cloudinary.models import CloudinaryField
from .helpers.identifier import make_identifier
from .instructor import Instructor


STATUS = (
    ('D', 'Draft'),
    ('P', 'Published'),
    ('R', 'For Review'),
    ('C', 'Cancelled')
)


class Plan(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    instructor = models.ForeignKey(Instructor, related_name='plans', on_delete=models.DO_NOTHING)

    # Determine if plan must be followed by registed students
    is_required = models.BooleanField(default=True)

    # This should be an integer representing percentages
    minimum_grade_required = models.IntegerField(null=True)

    # A clear description of what this study plan is about
    description = models.TextField()

    # Add raw content here or upload a file as needed
    content = models.TextField(blank=True)

    # Store study plans as files to be displayed on browser
    file = models.FileField(blank=True, upload_to='plans/%Y/%m/%d/', name='IEP')

    # Determine plan's eligibility and visibility
    status = models.CharField(max_length=2, choices=STATUS, default='D')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'student_plans'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()

        # Since using percentages, minimum_grade_required should be between 0 and 100
        if self.minimum_grade_required > 100 or self.minimum_grade_required < 0:
            raise ValidationError(
            gt_('Please provide a percentage value between 0 and 100')
            )

        # Ensure there's content for the plan. Either raw content or an uploaded file.
        if not self.content and self.file:
            raise ValidationError(
            gt_('Please provide either raw content or upload a file for this plan')
            )

        super().save(*args, **kwargs)

    def path_to_file(self):
        return self.file.url()

    def __str__(self):
        return self.created_at
