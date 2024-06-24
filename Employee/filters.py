import django_filters
from .models import * 

class EmployeeFilter(django_filters.FilterSet):
    address = django_filters.CharFilter(field_name='address',lookup_expr= 'istartswith')

    class Meta:
        model = Employee
        fields = ['address']
        