from django.db import models
from polymorphic.models import PolymorphicModel
from .helpers.identifier import make_identifier
from .question import Question


class Answer(PolymorphicModel):
    id = models.BigIntegerField(primary_key=True, editable=False)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.DO_NOTHING)

    # Default fields. Omit with the --no-defaults flag
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        db_table = 'answers'
        ordering = ['-created_at']
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.id = make_identifier()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.created_at


class BinaryAnswer(Answer):
    is_true = models.BooleanField(default=False)

    class Meta:
        db_table = 'answers_binary'


class ChoiceAnswer(Answer):
    content = models.CharField(max_length=256)

    class Meta:
        db_table = 'answers_choice'
