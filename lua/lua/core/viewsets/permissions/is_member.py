from rest_framework import permissions


class IsMemberOrNoAccess(permissions.IsAuthenticated):
    # TODO: Fix permission
    def has_object_permission(self, request, view, obj):
        user = request.user

        if obj.author:
            return obj.author == user
        if obj.owner:
            return obj.owner == user
        if obj.creator:
            return obj.creator == user
        if obj.instructor:
            return obj.instructor == user

        return False


class IsParticipantOrNoAccess(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.filter(username=request.user) or request.user == obj.owner
