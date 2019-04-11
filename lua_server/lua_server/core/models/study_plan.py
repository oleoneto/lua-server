from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as gl_
from ckeditor.fields import RichTextField
from .helpers.identifier import make_identifier
from .instructor import Instructor


class StudyPlan(models.Model):
    STATUS = (
        ('D', 'Draft'),
        ('P', 'Published'),
        ('R', 'For Review'),
        ('C', 'Cancelled')
    )

    id = models.BigIntegerField(primary_key=True, editable=False)

    # Instructor responsible for the plan
    creator = models.ForeignKey(Instructor, related_name='created_plans', on_delete=models.DO_NOTHING)

    # Short title capturing the essence of the plan
    title = models.CharField(max_length=250)

    # A clear description of what this study plan is about
    description = models.TextField(max_length=500)

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
        super().save(*args, **kwargs)

    @property
    def current_progress(self):
        # TODO: Implement
        # total completed modules / total number of modules
        return 0

    def __str__(self):
        return self.title


class StudyModule(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)

    plan = models.ForeignKey(StudyPlan, related_name='modules', on_delete=models.CASCADE)

    # Instructor responsible for the plan
    instructor = models.ForeignKey(Instructor, related_name='managed_modules', on_delete=models.DO_NOTHING)

    title = models.CharField(max_length=250)

    # Add raw content here or upload a file as needed
    content = RichTextField(blank=True)

    # Store study plans as files to be displayed on browser
    file = models.FileField(blank=True, upload_to='study-modules/%Y/%m/%d/', name='study-modules')

    # This should be an integer representing percentages
    minimum_grade_required = models.PositiveIntegerField(default=50)

    # Determine if plan must be followed by registered students
    is_required = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'study_modules'
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        # Since using percentages, minimum_grade_required should be between 0 and 100
        if self.minimum_grade_required > 100:
            raise ValidationError(
                gl_('Please provide a positive percentage value between 1 and 100')
            )

        # Ensure there's content for the plan. Either raw content or an uploaded file.
        if not self.content and self.file:
            raise ValidationError(
                gl_('Please provide either raw content or upload a file for this plan')
            )
        super().save(*args, **kwargs)

    def path_to_file(self):
        return self.file.url()


class StudyModuleRequirement(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    module = models.ForeignKey(StudyModule, related_name='requirements', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'study_module_requirements'
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
