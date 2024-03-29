from rest_framework import permissions


class IsStaffOrOwnerPermission(permissions.BasePermission):
     def has_object_permission(self, request, view, obj):
        if request.user == obj.storage.owner:
            return True
        if not request.user.is_staff:
            return False
        return True