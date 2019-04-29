from django.db import models
from django.core.exceptions import ValidationError
from .helpers.identifier import make_identifier
from .student import Student
from .course_offer import CourseOffer


class Waitlist(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, related_name='waitlists', on_delete=models.DO_NOTHING)
    course_offer = models.ForeignKey(CourseOffer, related_name='waitlists', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_waitlists'
        ordering = ['-created_at']
        unique_together = ('student', 'course_offer')

    def clean(self):
        super().clean()
        if self.student.id not in Student.objects.filter(id=self.student.id):
            raise ValidationError('Not a valid student account.')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'#{self.id}'
