from django.db import models


class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    STAFF = 1
    FACULTY = 2
    STUDENT = 3
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (FACULTY, 'Faculty'),
        (STAFF, 'Staff'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'school_roles'
        ordering = ['-created_at']

    @property
    def users_in_role(self):
        return self.users.count()

    def __str__(self):
        return self.get_id_display()
