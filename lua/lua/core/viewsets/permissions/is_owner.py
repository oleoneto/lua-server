from rest_framework import permissions

# TODO: Clear up permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAuthorOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsCreatorOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class IsOwnerOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsStudentOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user


class IsTeacherOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.teacher == request.user


class IsInstructorOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.instructor == request.user
