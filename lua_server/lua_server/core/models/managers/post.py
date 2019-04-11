# Remember to use the polymorphic to map models correctly
from polymorphic.managers import PolymorphicManager, PolymorphicQuerySet


class PostQuerySet(PolymorphicQuerySet):
    def public(self):
        return self.exclude(is_private=True)

    def published(self):
        return self.filter(status='P')

    def liked(self):
        return self.filter(likes__gt=0)


class PostManager(PolymorphicManager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def public(self):
        return self.published().public()

    def liked(self):
        return self.get_queryset().liked()
