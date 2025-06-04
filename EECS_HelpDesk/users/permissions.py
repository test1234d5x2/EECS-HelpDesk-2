from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.user_type == "admin"
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.user_type == "admin"
    

class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.user_type == 'admin'