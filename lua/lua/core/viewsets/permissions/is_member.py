from rest_framework import permissions
from ...models.student import Student
from ...models.instructor import Instructor


class IsMemberOrNoAccess(permissions.IsAuthenticated):
    # TODO: Fix permission
    def has_object_permission(self, request, view, obj):
        try:
            return obj.student.user == request.user
        except AttributeError:
            try:
                return obj.instructor.user == request.user
            except AttributeError:
                return False


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
        except Instructor.DoesNotExist:
            instructor = False
        try:
            student = Student.objects.get(user=request.user)
        except Student.DoesNotExist:
            student = False
        return obj.students.filter(student=student) or obj.course_instructor == instructor
