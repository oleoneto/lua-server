from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from ..models.post import Post
from ..models.post import Comment, Lecture, PostLike


class LikeAdminInline(admin.TabularInline):
    model = PostLike


class PostAdmin(PolymorphicChildModelAdmin):
    base_model = Post
    list_display = ['id', 'author', 'content', 'created_at', 'updated_at', 'status']


class CommentAdminInline(admin.StackedInline):
    model = Comment
    extra = 1
    fk_name = 'post'


@admin.register(Lecture)
class LectureAdmin(PostAdmin):
    base_model = Lecture
    show_in_index = True
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LikeAdminInline, CommentAdminInline]


@admin.register(Comment)
class CommentAdmin(PostAdmin):
    base_model = Comment
    show_in_index = True
    inlines = [LikeAdminInline]


@admin.register(Post)
class PostParentAdmin(PolymorphicParentModelAdmin):
    base_model = Post
    child_models = (Comment, Lecture)

    # Shows the concrete type of the object
    def obj_type(self, obj):
        return f"{ContentType.objects.get_for_id(obj.polymorphic_ctype_id)}".title()
    obj_type.short_description = "Type"

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = "Likes"

    # TODO: Fix this. Function is bypassed
    # def content(self, obj):
    #     return f"{obj.content[:20]}"
    # content.short_description = "Content Preview"

    list_display = ['id', 'obj_type', 'author', 'content', 'created_at', 'updated_at', 'status', 'likes_count']
