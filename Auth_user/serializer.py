from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField() 
    
    
class CoreUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoreUser  
        fields = "__all__" 