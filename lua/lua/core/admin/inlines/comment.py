from django.contrib import admin
from ...models.comment import Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

    # Ensure current user is assigned as author of post instance.
    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        obj.save()
