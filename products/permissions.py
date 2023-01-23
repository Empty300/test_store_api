from rest_framework import permissions


class IsOwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action not in ('create', 'update', 'destroy', 'retrieve'):
            return False
        else:
            return obj.user == request.user


class IsOwnerOrGetPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action not in ('create', 'update', 'destroy', 'retrieve'):
            return False
        elif view.action in 'retrieve':
            return True
        else:
            return obj.user == request.user
