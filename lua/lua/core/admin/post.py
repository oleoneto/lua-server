from django.contrib import admin
from ..models.post import Post
from .inlines.comment import CommentInline


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author']
    list_display = ['id', 'title', 'author', 'total_likes', 'total_comments', 'created_at', 'updated_at', 'is_inappropriate', 'is_draft']
    list_editable = ['is_draft']
    inlines = [CommentInline]

    # Ensure current user is assigned as author of post instance.
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()
