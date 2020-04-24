from rest_framework import permissions
from .models import Profile


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class PhonePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'basic']:
            return True
        elif view.action == 'create':
            return request.user.is_staff
        elif view.action == 'rate_phone':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy', 'edit_rating', 'delete_rating']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        if view.action in ['edit_rating', 'delete_rating']:
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False


class ProfilePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return obj.user == request.user or request.user.is_staff
        elif view.action in ['update', 'partial_update']:
            return obj.user == request.user
        else:
            return False


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_superuser
        elif view.action in ['create', 'retrieve', 'delete']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'create':
            return True
        elif view.action == 'retrieve':
            return request.user.is_superuser
        elif view.action == 'delete':
            return obj.user == request.user
        else:
            return False





