from django.db import models
from .helpers.identifier import make_identifier
from .helpers.student_identifier import make_student_id
from .user import User
from .study_plan import StudyPlan


class Student(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    user = models.OneToOneField(User, related_name='student_account', on_delete=models.PROTECT)
    student_id = models.CharField(max_length=30, unique=True, editable=False)
    date_of_birth = models.DateField(blank=True)
    is_active = models.BooleanField(default=True, help_text='Active or deactivate student account')
    plans = models.ManyToManyField(StudyPlan, help_text='Individual study plans for student', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_students'
        ordering = ['-created_at']

    @property
    def username(self):
        return self.user.username

    @property
    def name(self):
        return self.user.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        if not self.student_id:
            self.student_id = make_student_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.name
