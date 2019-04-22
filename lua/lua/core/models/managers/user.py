# Remember to use the polymorphic to map models correctly
from django.contrib.auth.models import UserManager as BaseUserManager
from polymorphic.managers import PolymorphicManager, PolymorphicQuerySet


class UserQuerySet(PolymorphicQuerySet):
    def public(self):
        return self.exclude(is_active=False)

    def instructors(self):
        return self.filter(status='P')

    def students(self):
        return self.filter(likes__gt=0)


class UserManager(PolymorphicManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def instructors(self):
        return self.get_queryset()

    def public(self):
        return self.get_queryset()

    def students(self):
        return self.get_queryset()


class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})
