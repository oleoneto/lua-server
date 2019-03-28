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
    is_private = models.BooleanField(default=False)

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
        return f"{self.id} - Post"


class Lecture(Post):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=False, allow_unicode=True)

    class Meta:
        db_table = 'post_lectures'

    def __str__(self):
        return f"{self.title}"


class Comment(Post):
    # Due to naming conflicts, this field will be called post instead of lecture
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
