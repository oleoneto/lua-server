from django.db import models
from .helpers.identifier import make_identifier
from .helpers.current_term import get_current_term
from .term import Term


class Course(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, max_length=700, help_text='What this course is about')
    enrollment_limit = models.PositiveIntegerField(default=100, help_text='Used to limit number of students per course')
    terms = models.ManyToManyField(Term, related_name='courses', help_text='Terms/seasons when the course is offered')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'courses'
        ordering = ['-created_at']

    def system_term(self):
        return get_current_term()

    @property
    def is_available(self):
        return self.enrollments.count() < self.enrollment_limit

    @property
    def available_in(self):
        return f'{self.terms.count()} term(s)'

    @property
    def students(self):
        return self.enrollments.count()

    @property
    def waitlisted(self):
        return self.waitlists.count()

    @property
    def students_enrolled(self):
        return f'{self.students}/{self.enrollment_limit}'

    @property
    def enrollment_progress(self):
        return int(self.enrollments.count() / self.enrollment_limit * 100)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
