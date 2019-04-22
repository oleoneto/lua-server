from django.db import models


class Term(models.Model):
    """
    Default terms to be used to control course availability.
    """
    SPRING = 1
    SUMMER = 2
    FALL = 3
    WINTER = 4
    TERM_CHOICES = (
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
    )

    id = models.PositiveSmallIntegerField(choices=TERM_CHOICES, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'terms'
        ordering = ['-created_at']

    @property
    def courses_offered(self):
        return self.courses.all()

    @property
    def total_courses_offered(self):
        return self.courses.count()

    # TODO: Fix this to account for repeated users
    @property
    def total_students_in_term(self):
        courses = self.courses.distinct()
        students = 0
        for course in courses:
            students += course.enrollments.distinct().count()
        return students

    @property
    def enrollment_percentage(self):
        enrollments = 0
        enrollment_limits = 0
        for course in self.courses.all():
            enrollments += course.enrollments.count()
            enrollment_limits += course.enrollment_limit

        return enrollments / enrollment_limits * 100

    def __str__(self):
        return self.get_id_display()
