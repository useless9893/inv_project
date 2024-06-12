from rest_framework import routers, serializers,viewsets
from.models import*


class Technology_optionSarializer(serializers.ModelSerializer):

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
