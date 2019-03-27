from django.db import models
from ckeditor.fields import RichTextField
from polymorphic.models import PolymorphicModel
from .helpers.identifier import make_identifier
from .user import User


STATUS = (
    ('D', 'Draft'),
    ('P', 'Published'),
    ('R', 'For Review')
)


class Post(PolymorphicModel):
    id = models.BigIntegerField(primary_key=True, editable=False)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    content = RichTextField()
    status = models.CharField(max_length=2, choices=STATUS, default='P')

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.content[:20]}..."


class Lecture(Post):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'post_lectures'


class Comment(Post):
    is_inappropriate = models.BooleanField(default=False)

    class Meta:
        db_table = 'post_comments'


class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_likes'
        unique_together = ('post', 'user')
