from django.contrib import admin

admin.site.site_header = "Olhares + Lua LMS"
admin.site.site_title = "Lua Learning Management System"

from .user import UserAdmin
from .event import EventAdmin
from .instructor import InstructorAdmin
from .logs import LogEntryAdmin
from .study_plan import StudyPlanAdmin
from .student import StudentAdmin
from .post import PostAdmin
from .enrollment import EnrollmentAdmin
from .course import CourseAdmin
from .comment import CommentAdmin
from .role import RoleAdmin
from .term import TermAdmin
from .waitlist import WaitlistAdmin
from .gradebook import GradebookAdmin
from .assignment import AssignmentAdmin, AssignmentTypeAdmin
from .learning_objective import LearningObjectiveAdmin
from .learning_level import LearningLevelAdmin
from .course_offer import CourseOfferAdmin
from .caderneta import CadernetaAdmin
