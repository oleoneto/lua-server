from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from polymorphic.models import PolymorphicModel
from .helpers.identifier import make_identifier
from .managers.post import PostManager
from .user import User


class Post(PolymorphicModel):
    STATUS = (
        ('D', 'Draft'),
        ('P', 'Published'),
        ('R', 'For Review')
    )

    id = models.BigIntegerField(primary_key=True, editable=False)
    author = models.ForeignKey(get_user_model(), related_name='posts', on_delete=models.DO_NOTHING, editable=False)
    content = RichTextField()
    status = models.CharField(max_length=2, choices=STATUS, default='P')
    is_private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    # Model managers
    objects = PostManager()

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - Post"


class Lecture(Post):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=False, allow_unicode=True)

    class Meta:
        db_table = 'post_lectures'

    def __str__(self):
        return f"{self.title}"


class Comment(Post):
    post = models.ForeignKey(Lecture, related_name='comments', on_delete=models.CASCADE)
    is_inappropriate = models.BooleanField(default=False)

    class Meta:
        db_table = 'post_comments'

    def __str__(self):
        return f"{self.id} - Comment"


class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_likes'
        unique_together = ('post', 'user')
