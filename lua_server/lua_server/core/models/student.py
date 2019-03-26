from django.db import models
from .helpers.identifier import make_identifier
from .user import User
from .plan import Plan


class Student(User):
    student_number = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True)
    plans = models.ManyToManyField(Plan)

    class Meta:
        db_table = 'user_students'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
