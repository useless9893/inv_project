from django.shortcuts import render
from rest_framework.response import Response
from .models import * 
from .serializer import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status


class EmployeeAPI(APIView):
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
            print('\n\n\n',user_obj,'\n\n\n')

            # city_data =  validated_data.pop('city_id')
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
        employee_obj = Employee.objects.get(employee_id=delete_employee)
        employee_obj.delete()
        return Response({'Message':"Employee deleted successfully"})









# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import Employee, City, State, Country, Role, CoreUser
# from .serializer import EmployeeSerializer

# class EmployeeAPI(APIView):
#     def get(self, request):
#         employee_obj = Employee.objects.all()
#         employee_serializer = EmployeeSerializer(employee_obj, many=True)
#         return Response(employee_serializer.data)

#     def post(self, request):
#         validated_data = request.data
#         employee_serializer = EmployeeSerializer(data=validated_data)
        
#         if employee_serializer.is_valid():
#             user_data = validated_data.pop('user_id')
#             user_obj = CoreUser.objects.create(**user_data)
#             user_obj.save()
            
#             city_id = validated_data.pop('city_id', None)
#             if not city_id:
#                 return Response({"Message": "City ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
#             city_instance = City.objects.filter(pk=city_id).first()
#             if not city_instance:
#                 return Response({"Message": "City not found"}, status=status.HTTP_400_BAD_REQUEST)
            
#             state_id = validated_data.pop('state_id', None)
#             if not state_id:
#                 return Response({"Message": "State ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
#             state_instance = State.objects.filter(pk=state_id).first()
#             if not state_instance:
#                 return Response({"Message": "State not found"}, status=status.HTTP_400_BAD_REQUEST)
            
#             country_id = validated_data.pop('country_id', None)
#             if not country_id:
#                 return Response({"Message": "Country ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
#             country_instance = Country.objects.filter(pk=country_id).first()
#             if not country_instance:
#                 return Response({"Message": "Country not found"}, status=status.HTTP_400_BAD_REQUEST)
            
#             role_id = validated_data.pop('role_id', None)
#             if not role_id:
#                 return Response({"Message": "Role ID is required"}, status=status.HTTP_400_BAD_REQUEST)
            
#             role_instance = Role.objects.filter(pk=role_id).first()
#             if not role_instance:
#                 return Response({"Message": "Role not found"}, status=status.HTTP_400_BAD_REQUEST)
            
#             employee_obj = Employee.objects.create(
#                 user_id=user_obj, 
#                 city_id=city_instance, 
#                 state_id=state_instance, 
#                 country_id=country_instance, 
#                 role_id=role_instance,
#                 **validated_data
#             )
#             return Response({"Message": "Employee created successfully"}, status=status.HTTP_201_CREATED)
        
#         return Response({"Message": employee_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request):
#         validated_data = request.data
#         employee_update = request.GET.get('employee_update')
        
#         employee_obj = Employee.objects.filter(employee_id=employee_update).first()
#         # if not employee_obj:
#         #     return Response({"Message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         employee_serializer = EmployeeSerializer(employee_obj, data=validated_data, partial=True)
        
#         if employee_serializer.is_valid():
#             employee_serializer.save()
#             return Response({'Message': 'Data updated successfully'}, status=status.HTTP_200_OK)
        
#         return Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request):
#         delete_employee = request.GET.get('delete_employee')
        
#         employee_obj = Employee.objects.filter(client_id=delete_employee).first()
#         # if not employee_obj:
#         #     return Response({"Message": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         employee_obj.delete()
#         return Response({'Message': "Employee deleted successfully"}, status=status.HTTP_200_OK)



