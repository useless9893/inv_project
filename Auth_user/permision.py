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


         

         
    

    

    
         
