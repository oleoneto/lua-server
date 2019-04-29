from django.db import models
from .helpers.identifier import make_identifier
from .instructor import Instructor
from .learning_objective import LearningObjective


class StudyPlan(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)

    # Instructor responsible for the plan
    creator = models.ForeignKey(Instructor, related_name='created_plans', on_delete=models.PROTECT)

    # Short title capturing the essence of the plan
    title = models.CharField(max_length=250)

    # A clear description of what this study plan is about
    description = models.TextField(max_length=500)

    # Determine plan's eligibility and visibility
    learning_objectives = models.ManyToManyField(LearningObjective, related_name='study_plans', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_student_plans'
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

    # @property
    # def students(self):
    #     return Student.registered.filter_by_instance(instance=self)

    def __str__(self):
        return self.title
