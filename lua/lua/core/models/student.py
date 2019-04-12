from django.db import models
from .helpers.identifier import make_identifier
from .helpers.student_identifier import make_student_id
from .user import User
from ..models.study_plan import StudyPlan


class Student(User):
    student_id = models.CharField(max_length=30, unique=True, editable=False)
    date_of_birth = models.DateField(blank=True)
    plans = models.ManyToManyField(StudyPlan)

    class Meta:
        db_table = 'user_students'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        if not self.student_id:
            self.student_id = make_student_id()
        super().save(*args, **kwargs)
