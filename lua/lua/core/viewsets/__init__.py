from rest_framework import routers

# Users
from .user import UserViewSet
from .guest import GuestViewSet
from .instructor import InstructorViewSet
from .student import StudentViewSet

# Agenda
from .event import EventViewSet

# Classroom
# from .module import ModuleViewSet
from .study_plan import StudyPlanViewSet

# Postings and articles
from .post import PostViewSet
from .lecture import LectureViewSet
from .comment import CommentViewSet

from .gradebook import GradebookViewSet
from .enrollment import EnrollmentViewSet
from .course import CourseViewSet

# Routing manager for all viewsets
router = routers.SimpleRouter(trailing_slash=False)

# View-set registration
router.register('users', UserViewSet)
router.register('guests', GuestViewSet)
router.register('instructors', InstructorViewSet)
router.register('students', StudentViewSet)


router.register('enrollments', EnrollmentViewSet)
router.register('gradebooks', GradebookViewSet)
router.register('courses', CourseViewSet)


router.register('events', EventViewSet)
router.register('calendar', EventViewSet)


# router.register('modules', ModuleViewSet)
router.register('study-plans', StudyPlanViewSet)


router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('lectures', LectureViewSet)
