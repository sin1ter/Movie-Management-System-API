from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always return True for read operations.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.created_by == request.user
    
class IsOwnerOrReadOnly1(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always return True for read operations.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user