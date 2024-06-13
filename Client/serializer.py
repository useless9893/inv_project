from rest_framework import routers, serializers,viewsets
from.models import*
from Auth_user.serializer import *




class ClientSerializer(serializers.ModelSerializer):
    user_id =CoreUserSerializer()
    class Meta:
        model = Client
        fields = '__all__'
        
        
class Client2Serializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user_id.first_name')
    last_name = serializers.CharField(source='user_id.last_name')
    user_name = serializers.CharField(source='user_id.user_name')
    contact = serializers.CharField(source='user_id.contact')
    email = serializers.CharField(source='user_id.email')
    class Meta:
        model = Client
        fields = ['user_name','client_name','first_name','last_name','email','contact','company_address']
        # fields = '__all__'
    
    def create(self,data):
        print('data',data)    
        
class Technology_optionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology_option
        fields = '__all__'




class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = '__all__'



class Payment_methodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment_method
        fields = '__all__'



class TaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tax
        fields = '__all__'
