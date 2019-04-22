from django.contrib import admin
from ..models.comment import Comment


# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ['author']
    list_display = ['id', 'post', 'author', 'created_at', 'updated_at']

    # Ensure current user is assigned as author of post instance.
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()
