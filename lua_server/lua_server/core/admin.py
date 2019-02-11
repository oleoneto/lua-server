from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin, UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from .models.user import User
from .models.post import Post, Lecture, Comment, PostLike
from .models.plan import Plan
from .models.planner import Planner
from .models.instructor import Instructor
from .models.student import Student


admin.site.site_header = "Lua Dashboard"
admin.site.site_title = "Lua Dashboard"


# Users
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ['id', 'username', 'name', 'is_staff']
    prepopulated_fields = {'username': ('first_name', 'last_name',)}
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password', 'profile_picture')
        }),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'profile_picture'),
        }),
    )

    search_fields = ('email', 'username', 'first_name', 'last_name')


# Instructors and Students
class PlanInline(admin.TabularInline):
    model = Plan

class PlannerInline(admin.TabularInline):
    model = Planner


@admin.register(Instructor)
class InstructorAdmin(UserAdmin):
    inlines = [PlannerInline, PlanInline]



# Posts, Comments, and Likes
class LikeAdminInline(admin.TabularInline):
    model = PostLike


class PostAdmin(PolymorphicChildModelAdmin):
    base_model = Post
    list_display = ['id', 'author', 'content', 'created_at', 'updated_at', 'status']


@admin.register(Lecture)
class LectureAdmin(PostAdmin):
    base_model = Lecture
    show_in_index = True
    prepopulated_fields = {'slug': ('title',)}
    inlines = [LikeAdminInline]


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

    list_display = ['id', 'obj_type', 'author', 'content', 'created_at', 'updated_at', 'status', 'likes_count']


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    # readonly_fields = LogEntry._meta.get_fields()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag_',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def action_flag_(self, obj):
        flags = {
            1: "Addition",
            2: "Changed",
            3: "Deleted",
        }
        return flags[obj.action_flag]

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'
