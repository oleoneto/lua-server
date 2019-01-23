from django.db import models
from polymorphic.models import PolymorphicModel
from .helpers.identifier import make_identifier
from .user import User
from .course import Course


STATUS = (
    ('D', 'Draft'),
    ('P', 'Published'),
    ('R', 'For Review')
)


class Post(PolymorphicModel):
    id = models.BigIntegerField(primary_key=True, editable=False)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    content = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS, default='P')
    date_published = models.DateField()
    
    # Default fields. Omit with the --no-defaults flag
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
        return self.id


class Lecture(Post):
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique_for_month=True)
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'post_lectures'


class Comment(Post):
    is_inappropriate = models.BooleanField(default=False)

    class Meta:
        db_table = 'post_comments'


class PostLikes(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.SET_NULL)
    user = models.ForeignKey(User, related_name='likes', on_delete=models.SET_NULL)

    class Meta:
        db_table = 'post_likes'
