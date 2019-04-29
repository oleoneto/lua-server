from django.db import models
from .helpers.identifier import make_identifier


class LearningObjective(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=250, help_text='What should we call this learning objective?')
    description = models.TextField(help_text='Describe what this learning objective seeks to accomplish')
    is_required = models.BooleanField(default=True, help_text='Determine if the objective is mandatory')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_learning_objectives'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def grade_requirement(self):
        grade = 0
        total_outcomes = 0
        for outcome in self.outcomes.all():
            if outcome.is_graded:
                grade += outcome.grade_requirement
                total_outcomes += 1
        return grade / total_outcomes if total_outcomes > 0 else 0

    @property
    def total_files(self):
        return self.files.count()

    @property
    def total_outcomes(self):
        return self.outcomes.count()

    def __str__(self):
        return self.title


class LearningObjectiveFile(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    learning_objective = models.ForeignKey(LearningObjective,
                                           related_name='files', on_delete=models.DO_NOTHING)

    # If there is a file associated with the learning objective, it can be saved here
    file = models.FileField(upload_to='learning-objectives/%Y/%m/%d/', name='learning-objectives')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_learning_objective_files'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)


class LearningLevel(models.Model):
    """
    Default outcome levels to be used to control outcome groupings.
    """
    KNOWLEDGE = 1
    COMPREHENSION = 2
    APPLICATION = 3
    ANALYSIS = 4
    SYNTHESIS = 5
    EVALUATION = 6
    CRITICAL_THINKING = 7

    TERM_CHOICES = (
        (KNOWLEDGE, 'Knowledge'),
        (COMPREHENSION, 'Comprehension'),
        (APPLICATION, 'Application'),
        (ANALYSIS, 'Analysis'),
        (SYNTHESIS, 'Synthesis'),
        (EVALUATION, 'Evaluation'),
        (CRITICAL_THINKING, 'Critical Thinking'),
    )

    id = models.PositiveSmallIntegerField(choices=TERM_CHOICES, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_learning_levels'
        ordering = ['-created_at']

    def __str__(self):
        return self.get_id_display()


class LearningOutcome(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    learning_objective = models.ForeignKey(LearningObjective,
                                           related_name='outcomes', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250)
    description = models.TextField()
    is_graded = models.BooleanField(default=True, help_text='Specifies if the outcome counts towards overall grade')
    grade_requirement = models.PositiveIntegerField(default=100, help_text='Minimum passing grade for your students')
    learning_levels = models.ManyToManyField(LearningLevel, related_name='outcomes', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_learning_objective_outcomes'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
