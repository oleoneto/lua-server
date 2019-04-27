from django.db import models
from .abstract.post import BasePost
from .user import User
from .managers.post import PostManager


class Post(BasePost):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    flags = models.ManyToManyField(User, related_name='post_flags', blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    objects = PostManager()

    class Meta:
        db_table = 'core_posts'
        ordering = ['-created_at']

    @property
    def is_inappropriate(self):
        return self.flags.count() >= 10

    @property
    def has_likes(self):
        return self.likes.count() > 0

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_comments(self):
        return self.comments.count()
