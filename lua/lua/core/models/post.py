from django.db import models
from .abstract.post import BasePost
from .user import User


class Post(BasePost):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING, editable=False)
    flags = models.ManyToManyField(User, related_name='post_flags')
    likes = models.ManyToManyField(User, related_name='post_likes')

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    @property
    def is_inappropriate(self):
        return self.flags.count() >= 10

    @property
    def has_likes(self):
        return self.likes.count() > 0
