from django.db import models
from .helpers.identifier import make_identifier
from .user import User
from .course import Course
from .assignment import Assignment


class Gradebook(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(User, related_name='gradebooks', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, related_name='gradebooks', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'gradebooks'
        ordering = ['-created_at']
        
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
        db_table = 'gradebook_assignment_entries'
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
        db_table = 'gradebook_note_entries'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Note #{self.id}'
