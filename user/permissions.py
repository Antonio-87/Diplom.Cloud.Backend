from rest_framework import permissions


class isStaffEditorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True if request.user.is_staff else False


class isStaffOrUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return False if request.user != obj.user or not request.user.is_staff else True