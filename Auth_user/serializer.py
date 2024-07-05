from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField() 
    

   
    
class CoreUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoreUser  
        fields = ["user_id",'user_name','first_name','last_name','email','contact']
        
        
class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = ['country_id','country_name']        
class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = ['state_id','state_name']        
class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = ['city_id','city_name']        