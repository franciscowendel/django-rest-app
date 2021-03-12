from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_super_user:
                return True
            return False
        return True
