from rest_framework import routers

# Users
from .user import UserViewSet
from .guest import GuestViewSet
from .instructor import InstructorViewSet
from .student import StudentViewSet

# Agenda
from .event import EventViewSet

# Postings and articles
from .post import PostViewSet
from .lecture import LectureViewSet
from .comment import CommentViewSet

# Classroom
# from .module import ModuleViewSet
from .study_plan import StudyPlanViewSet
from .gradebook import GradebookViewSet
from .enrollment import EnrollmentViewSet
from .course import CourseViewSet
from .assignment import AssignmentViewSet
from .learning_objective import LearningObjectiveViewSet

# Routing manager for all viewsets
router = routers.SimpleRouter(trailing_slash=False)

# View-set registration
router.register('users', UserViewSet)
router.register('guests', GuestViewSet)
router.register('instructors', InstructorViewSet)
router.register('students', StudentViewSet)


router.register('assignments', AssignmentViewSet)
router.register('enrollments', EnrollmentViewSet)
router.register('gradebooks', GradebookViewSet)
router.register('courses', CourseViewSet)


router.register('events', EventViewSet)


# router.register('modules', ModuleViewSet)
router.register('study-plans', StudyPlanViewSet)
router.register('learning-objectives', LearningObjectiveViewSet)


router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('lectures', LectureViewSet)
