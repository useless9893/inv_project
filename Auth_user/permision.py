from .models import CoreUser
from rest_framework import permissions


class IsClientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method not in ['GET','POST']:
            return False
        
        if hasattr(request.user,'is_client'):
            if not request.user:
                return False
        return True 

    

class IsEmployeePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method not in ['GET','POST']:
            return False
        
        if hasattr(request.user,'is_employee'):
            if not request.user:
                return False
        return True 










# class CoreUserPermision(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return False
    
#     def has_object_permission(self, request, view, obj):


#         if request.user.is_client == True:
#             return True
#         # return obj.CoreUser == request.CoreUser
#         return False
         

# class Employeepermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return False
    
#     def has_object_permission(self, request, view, obj):
#         if request.CoreUser.is_employee == True:
#             return True
         

         
    

    

    
         
