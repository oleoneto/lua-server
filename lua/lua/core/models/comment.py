from django.db import models
from .helpers.identifier import make_identifier
from ckeditor.fields import RichTextField
from .user import User
from .post import Post


class Comment(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=False)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, editable=False)
    content = RichTextField()
    flags = models.ManyToManyField(User, related_name='comment_flags', blank=True)
    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']

    @property
    def is_inappropriate(self):
        return self.flags.count() >= 10

    @property
    def has_likes(self):
        return self.likes.count() > 0

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} by {self.author.username}'
