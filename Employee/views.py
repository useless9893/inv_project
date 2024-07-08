from django.shortcuts import render
from rest_framework.response import Response
from .models import * 
from .serializer import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from Auth_user.permision import IsEmployeePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from django.core.mail import EmailMessage



class EmployeeAPI(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsEmployeePermission]
    
    def get(self,request):
        employee_obj = Employee.objects.all()
        employee_serializer = EmployeeSerializer(employee_obj,many=True)
        return Response(employee_serializer.data)
    
    def post(self,request):
        validated_data = request.data 
        employee_serializer = EmployeeSerializer(data=validated_data)
        if employee_serializer.is_valid():
            user_data = validated_data.pop('user_id')
            user_obj = CoreUser.objects.create(**user_data)
            user_obj.set_password(user_data['password'])
            user_obj.save()
            
            city_obj = City.objects.get(city_id=validated_data['city_id'])
            state_obj = State.objects.get(state_id=validated_data['state_id'])
            country_obj = Country.objects.get(country_id=validated_data['country_id'])
            role_obj = Role.objects.get(role_id=validated_data['role_id'])
           
            employee_obj = Employee.objects.create(user_id=user_obj, 
                                                   city_id = city_obj,
                                                   state_id = state_obj,
                                                   country_id = country_obj,
                                                   role_id = role_obj,
                                                   pincode=validated_data['pincode'],
                                                   address=validated_data['address'],
                                                   id_proof=validated_data['id_proof'],
                                                   salary=validated_data['salary'],
                                                   age=validated_data['age'])
            

            email = user_data['email']
            message = EmailMessage(
                'Test email subject',
                'test email body,  client create successfully ',
                settings.EMAIL_HOST_USER,
                [email]
            )
            message.send(fail_silently=False)
            
            return Response({"Message":"Employee created successfully"})
        
        else:
            return Response({"Message":employee_serializer.errors})  
    


    def put(self,request):
        validated_data = request.data
        employee_obj = Employee.objects.get(employee_id=validated_data['employee_id'])
       
        employee_serializer = EmployeeSerializer(employee_obj,data=validated_data,partial=True)
        
        if employee_serializer.is_valid():
            employee_serializer.save()
            return Response({"message":"data updated successfully","data":employee_serializer.data} )
        
        else:
            return Response(employee_serializer.errors)  
     
    def delete(self,request):
        delete_employee = request.GET.get('delete_employee')
        employee_obj = CoreUser.objects.get(user_id=delete_employee)
        employee_obj.delete()
        return Response({'Message':"Employee deleted successfully"})



# class EmployeeListView(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     filter_backends = [SearchFilter , DjangoFilterBackend]
#     filterset_class = EmployeeFilter


@api_view(['GET'])                  # Apply filtering in Employee model
def EmployeeFilter(request):
    employee = request.GET.get('first_name',None)

    if employee:
        employee_obj = Employee.objects.filter(user_id__first_name=employee)
        serializer_obj = EmployeeSerializer(employee_obj,many=True)
        return Response(serializer_obj.data)









