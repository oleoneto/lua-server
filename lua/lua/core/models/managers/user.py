# Remember to use the polymorphic to map models correctly
from polymorphic.managers import PolymorphicManager, PolymorphicQuerySet


class UserQuerySet(PolymorphicQuerySet):
    def public(self):
        return self.exclude(is_active=False)

    def instructors(self):
        return self.filter(status='P')

    def students(self):
        return self.filter(likes__gt=0)


class UserManager(PolymorphicManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def instructors(self):
        return self.get_queryset()

    def public(self):
        return self.get_queryset()

    def students(self):
        return self.get_queryset()
