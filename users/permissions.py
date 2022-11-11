from rest_framework import permissions


class SameUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if (request.method == 'PUT' or request.method == 'PATCH') and view.kwargs['id'] != request.user.id:
            return False
        return True
