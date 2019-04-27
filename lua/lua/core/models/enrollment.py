from django.db import models
from .helpers.identifier import make_identifier
from .helpers.mailer import send_mail
from .student import Student
from .waitlist import Waitlist
from .gradebook import Gradebook
from .course_offer import CourseOffer


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
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.DO_NOTHING)
    course_offer = models.ForeignKey(CourseOffer, related_name='enrollments', on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_enrollments'
        ordering = ['-created_at']
        unique_together = ('student', 'course_offer',)

    def save(self, *args, **kwargs):
        will_notify = False
        if not self.id:
            self.id = make_identifier()
            will_notify = True
        if self.course_offer.enrollments.count() >= self.course_offer.enrollment_limit:
            Waitlist.objects.get_or_create(student=self.student, course_offer=self.course_offer)
            print(f"Course if full. Student {self.student.username} added to waitlist.")
            return
        super().save(*args, **kwargs)

        # Create Gradebook for user
        Gradebook.objects.get_or_create(student=self.student, course_offer=self.course_offer)

        if will_notify:
            send_mail(user=self.student.user, subject=f"Lua: Enrollment confirmation #{self.id}",
                      message=f'{ENROLLMENT_MESSAGE.format(self.student.name, self.course_offer.course, self.course_offer.course.id, self.student.gradebooks.last(), self.id)}')

        try:
            # Attempt to remove user from waiting list if enrollment is successful
            instance = Waitlist.objects.get(student=self.student, course_offer=self.course_offer)
            instance.delete()
        except Waitlist.DoesNotExist:
            return

    def delete(self, using=None, keep_parents=False):
        waiting_instance = Waitlist.objects.first()
        super().delete()

        if waiting_instance:
            try:
                # Attempt to enroll first user in waiting list
                Enrollment.objects.create(student=waiting_instance.student, course_offer=waiting_instance.course_offer)
                waiting_instance.delete()
            except Waitlist.DoesNotExist:
                return

    @property
    def course(self):
        return self.course_offer.course

    @property
    def course_instructor(self):
        return self.course_offer.instructor

    @property
    def students(self):
        return self.course_offer.enrollments.filter(course_offer=self.course_offer)

    def __str__(self):
        return f'#{self.id}'
