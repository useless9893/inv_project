from .models import CoreUser
from rest_framework.permissions import BasePermission
from rest_framework import permissions





class CoreUserPermision(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):


        if request.user.is_client == True:
            return True
        # return obj.CoreUser == request.CoreUser
        return False
         

class Employeepermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.CoreUser.is_employee == True:
            return True
         

         
    

    

    
         
