from django.db import models
from .helpers.identifier import make_identifier
from .helpers.mailer import send_mail
from .user import User
from .course import Course
from .waitlist import Waitlist
from .gradebook import Gradebook
from .role import Role


ENROLLMENT_MESSAGE = """
Congratulations {},

You are now enrolled in the course {} #{}. 
You can monitor your progress in the course by checking your gradebook {}.

Your enrollment verification number is #{}.

Sincerely,
Admin @ LuaLMS
"""


class Enrollment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    student = models.ForeignKey(User, related_name='enrollments', on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'enrollment'
        ordering = ['-created_at']
        unique_together = ('student', 'course',)

    def save(self, *args, **kwargs):
        will_notify = False
        if not self.id:
            self.id = make_identifier()
            will_notify = True
        if self.course.enrollments.count() >= self.course.enrollment_limit:
            Waitlist.objects.get_or_create(student=self.student, course=self.course)
            print(f"Course if full. Student {self.student.username} added to waitlist.")
            return
        super().save(*args, **kwargs)

        # Create Gradebook for user
        Gradebook.objects.get_or_create(student=self.student, course=self.course)

        if will_notify:
            send_mail(user=self.student, subject=f"Lua: Enrollment confirmation #{self.id}",
                      message=f'{ENROLLMENT_MESSAGE.format(self.student.name, self.course.name, self.course.id, self.student.gradebooks.last(), self.id)}')

        try:
            # Attempt to remove user from waiting list if enrollment is successful
            instance = Waitlist.objects.get(student=self.student, course=self.course)
            instance.delete()
        except Waitlist.DoesNotExist:
            return

    def delete(self, using=None, keep_parents=False):
        waiting_instance = Waitlist.objects.first()
        super().delete()

        if waiting_instance:
            try:
                # Attempt to enroll first user in waiting list
                Enrollment.objects.create(student=waiting_instance.student, course=waiting_instance.course)
                waiting_instance.delete()
            except Waitlist.DoesNotExist:
                return

    def __str__(self):
        return f'#{self.id}'
