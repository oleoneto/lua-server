from django.db import models
from .helpers.identifier import make_identifier
from .student import Student
from .study_plan import StudyPlan


class Caderneta(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(Student, related_name='cadernetas', on_delete=models.PROTECT)
    study_plan = models.ForeignKey(StudyPlan, related_name='cadernetas', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_cadernetas'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'#{self.id} - {self.student.user.name}'
