from rest_framework import permissions


class IsStaffOrOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False if request.user != obj.owner or not request.user.is_staff else True