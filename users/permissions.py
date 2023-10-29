from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        for user in view.get_object().user.all():
            if request.user == user:
                return True
        return False


class IsSuperuser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
