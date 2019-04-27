from django.db import models
from django.core.exceptions import ValidationError
from .helpers.identifier import make_identifier
from .term import Term
from .course import Course
from .instructor import Instructor


class CourseOffer(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    course = models.ForeignKey(Course, related_name='offers', on_delete=models.DO_NOTHING)
    term = models.ForeignKey(Term, related_name='courses_offered', on_delete=models.DO_NOTHING)
    instructor = models.ForeignKey(Instructor, related_name='courses_taught', on_delete=models.DO_NOTHING)

    # Substitute fixed start and end with RecurrenceField
    start_date = models.DateField(help_text='Date when classes will begin')
    end_date = models.DateField(help_text='Date when classes will end')

    enrollment_limit = models.PositiveIntegerField(default=50, help_text='Limit the number of students in course')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_course_offers'
        ordering = ['-created_at']

    def clean(self):
        super().clean()
        if self.start_date > self.end_date:
            raise ValidationError('Start date should be before end date')

        # TODO: Check if term and dates match

        # TODO: Check if course offer already exists
        if CourseOffer.objects.filter(course=self.course, instructor=self.instructor, term=self.term):
            raise ValidationError('Course is already being offered')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    @property
    def course_name(self):
        return self.course.name

    @property
    def waitlisted(self):
        return self.waitlists.count()

    def __str__(self):
        return f'{self.course.name} {self.id}'
