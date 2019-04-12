from django.db import models
from .helpers.identifier import make_identifier
from datetime import timedelta, datetime
from .instructor import Instructor
from .user import User


def when_exam_is_due():
    return datetime.now() + timedelta(days=7)


class Exam(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)

    # This user will be responsible for maintaining the exam
    instructor = models.ForeignKey(Instructor, related_name='exams', on_delete=models.DO_NOTHING)

    # i.e Physics 101 - Exam 1
    title = models.CharField(max_length=250)

    # Test your knowledge of gravity, velocity, acceleration, and conservation of energy
    summary = models.TextField(blank=True)

    # When the exam can no longer be accessed
    due_date = models.DateTimeField(default=when_exam_is_due)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'exams'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def is_available(self):
        return self.due_date > datetime.now()
    
    def __str__(self):
        return self.title


class ExamQuestion(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    exam = models.ForeignKey(Exam, related_name='exam_questions', on_delete=models.CASCADE)
    text = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'exam_questions'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id}'


class ExamResponse(models.Model):
    question = models.ForeignKey(ExamQuestion, related_name='responses', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='responses', on_delete=models.DO_NOTHING)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'exam_responses'
        ordering = ['created_at']

    def __str__(self):
        return self.text
