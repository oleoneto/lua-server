from django.contrib import admin
from ..models.learning_objective import LearningLevel


@admin.register(LearningLevel)
class LearningLevelAdmin(admin.ModelAdmin):
    pass
