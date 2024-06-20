import django_filters
from  .models import *

class ClientFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client_name', lookup_expr='istartswith')
    

    class Meta:
        model = Client
        fields = ['client_name']

