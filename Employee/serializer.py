from rest_framework import routers, serializers,viewsets
from .models import *
from Auth_user.models import *
from Auth_user.serializer import *

 
 

class EmployeeSerializer(serializers.ModelSerializer):
    user_id =CoreUserSerializer()
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    state_id = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    country_id = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'



