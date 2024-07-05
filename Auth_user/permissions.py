from rest_framework import permissions
from .models import CoreUser

class IsClientOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
    

    def has_object_permission(self, request, view, obj):
        if request.CoreUser.is_client == True:
            return True
        return obj.CoreUser == request.CoreUser
    

class IsEmployeeOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.CoreUser.is_employee == True:
            return True
        return obj.CoreUser == request.CoreUser