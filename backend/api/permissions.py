from rest_framework import permissions


class IsAuthorOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user == obj.worker
                )


class IsAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.user.is_authenticated
                and request.user.is_admin)
