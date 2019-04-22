from django.db import models
from .helpers.identifier import make_identifier
from .student import Student
from .course import Course


class Enrollment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'enrollment'
        ordering = ['-created_at']
        unique_together = ('student', 'course',)
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.student} in {self.course.name}'
