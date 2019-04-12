from django.contrib import admin
from .user import UserAdmin
from .event import EventAdmin
from .instructor import InstructorAdmin
from .logs import LogEntryAdmin
from .study_plan import StudyPlanAdmin
from .planner import PlannerAdmin
from .post import PostAdmin, LectureAdmin, CommentAdmin
from .student import StudentAdmin


admin.site.site_header = "Lua Learning Platform"
admin.site.site_title = "Lua Learning Platform"
