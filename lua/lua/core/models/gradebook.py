from django.db import models
from .helpers.identifier import make_identifier
from .assignment import Assignment
from .course_offer import CourseOffer
from .student import Student


class Gradebook(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, related_name='gradebooks', on_delete=models.PROTECT)
    course_offer = models.ForeignKey(CourseOffer, related_name='gradebooks', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_gradebooks'
        ordering = ['-created_at']

    @property
    def course(self):
        return self.course_offer.course

    @property
    def course_instructor(self):
        return self.course_offer.instructor

    @property
    def students(self):
        return self.course_offer.enrollments.filter(course_offer=self.course_offer)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'#{self.id}'


class GradebookAssignmentEntry(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    gradebook = models.ForeignKey(Gradebook, related_name='assignment_entries', on_delete=models.DO_NOTHING)
    assignment = models.ForeignKey(Assignment, related_name='gradebook_entries', on_delete=models.DO_NOTHING)
    grade = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_gradebook_assignment_entries'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Assignment entry #{self.id}'


class GradebookNoteEntry(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    gradebook = models.ForeignKey(Gradebook, related_name='note_entries', on_delete=models.DO_NOTHING)
    note = models.TextField(max_length=700)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_gradebook_note_entries'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Note #{self.id}'
