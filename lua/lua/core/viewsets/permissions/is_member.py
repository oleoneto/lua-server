from rest_framework import permissions
from ...models.student import Student
from ...models.instructor import Instructor


class IsMemberOrNoAccess(permissions.IsAuthenticated):
    # TODO: Fix permission
    def has_object_permission(self, request, view, obj):
        return obj.members.filter(user=request.user)


class IsParticipantOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.participants.filter(username=request.user) or request.user == obj.owner


class IsStudentOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        try:
            student = Student.objects.get(user=request.user)
            return obj.students.filter(student_id=student.id)
        except Student.DoesNotExist:
            return False


class IsInCourseNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        try:
            instructor = Instructor.objects.get(user=request.user)
            return obj.course_instructor == instructor
        except Instructor.DoesNotExist:
            try:
                student = Student.objects.get(user=request.user)
                return obj.students.filter(student_id=student.id)
            except Student.DoesNotExist:
                return False
