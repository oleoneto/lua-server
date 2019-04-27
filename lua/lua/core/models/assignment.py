import uuid
from django.db import models
from django.core.exceptions import ValidationError
from .helpers.identifier import make_identifier
from .helpers.assignment import assignment_filepath, assignment_submission_path, get_due_date
from ckeditor.fields import RichTextField
from .course_offer import CourseOffer


class AssignmentType(models.Model):
    """
    Default assignment types.
    """
    HOMEWORK = 1
    QUIZ = 2
    PROJECT = 3
    REPORT = 4
    ESSAY = 5
    TEST = 6
    ASSIGNMENT_CHOICES = (
        (HOMEWORK, 'Homework'),
        (QUIZ, 'Quiz'),
        (PROJECT, 'Project'),
        (REPORT, 'Report'),
        (ESSAY, 'Essay'),
        (TEST, 'Test'),
    )
    id = models.PositiveIntegerField(choices=ASSIGNMENT_CHOICES, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignment_types'

    def assignment_count(self):
        return self.assignments.count()

    @property
    def description(self):
        return self.get_id_display()

    def __str__(self):
        return self.get_id_display()


class Assignment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    course_offer = models.ForeignKey(CourseOffer, related_name='assignments', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(default=get_due_date)
    points = models.IntegerField(default=100, help_text='Specify how many points this assignment is worth')
    assignment_type = models.ForeignKey(AssignmentType, related_name='assignments',
                                        default=AssignmentType.HOMEWORK, on_delete=models.DO_NOTHING)
    public = models.BooleanField(default=True)
    access_code = models.UUIDField(default=uuid.uuid4, unique=True,
                                   help_text='Code for students searching for your course')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignments'
        ordering = ['-created_at']

    @property
    def course(self):
        return self.course_offer.course.name

    @property
    def total_file_submissions(self):
        return self.file_submissions.count()

    @property
    def total_files(self):
        return self.files.count()

    @property
    def total_questions(self):
        return self.questions.count()

    def clean(self):
        if not self.public and not self.access_code:
            raise ValidationError('This course is private, so you must provide an access code for your students')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name


class AssignmentFile(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    assignment = models.ForeignKey(Assignment, related_name='files', on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=assignment_filepath, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignment_files'
        ordering = ['-created_at']

    def __str__(self):
        return f'File #{self.id} for {self.assignment.name}'


class Question(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    assignment = models.ForeignKey(Assignment, related_name='questions', on_delete=models.DO_NOTHING)
    question = RichTextField()
    number = models.PositiveIntegerField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignment_questions'
        ordering = ['-created_at', 'number']
        unique_together = ('assignment', 'number')

    @property
    def total_answers(self):
        return self.answers.count()

    @property
    def student_answers(self):
        return self.answers.all()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question


class Option(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    question = models.ForeignKey(Question, related_name='options', on_delete=models.DO_NOTHING)
    option = models.CharField(blank=True, max_length=250)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignment_question_options'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.option


class Answer(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.DO_NOTHING)
    answer = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignment_question_answers'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def question_options(self):
        return self.question.options.all()

    def __str__(self):
        return self.answer


class FileSubmission(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    assignment = models.ForeignKey(Assignment, related_name='file_submissions', on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=assignment_submission_path)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_assignment_file_submissions'
        ordering = ['-created_at']

    def __str__(self):
        return f'Submission #{self.id} for {self.assignment.name}'
