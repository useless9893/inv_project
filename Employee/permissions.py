from rest_framework.permissions import BasePermission


class IsEmployeeOwner(BasePermission):
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        return obj.Employee == request.Employee
    