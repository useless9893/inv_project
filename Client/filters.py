import django_filters
from  .models import *

class ClientFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client_name', lookup_expr='istartswith')
    

    class Meta:
        model = Client
        fields = ['client_name']



# class ProjectFilter(django_filters.FilterSet):
#     project_name = django_filters.CharFilter(field_name='project_name', lookup_expr='istartswith')

#     class Meta:
#         model = Project
#         fields = ['project_name']




# class InvoiceFilter(django_filters.FilterSet):
#     invoice_id = django_filters.NumberFilter(field_name='invoice_id')

#     class Meta:
#         model = Invoice
#         fields = ['invoice_id']

