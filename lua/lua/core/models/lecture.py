from django.db import models
from .abstract.post import BasePost
from .user import User


class Lecture(BasePost):
    author = models.ForeignKey(User, related_name='lectures', on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='lecture_likes', blank=True)

    class Meta:
        db_table = 'school_lectures'
        ordering = ['-created_at']

    @property
    def has_likes(self):
        return self.likes.count() > 0
