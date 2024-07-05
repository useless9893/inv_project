import django_filters
from  .models import *

class ClientFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client_name', lookup_expr='istartswith')
    client_id = django_filters.NumberFilter(field_name='client_id', lookup_expr='istartswith')
    

    class Meta:
        model = Client
        fields = ['client_name','client_id']


class TechnologyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name',lookup_expr='istartswith')

    class Meta:
        model = Technology
        fields = ['name']



class TeamFilter(django_filters.FilterSet):
    team_name = django_filters.CharFilter(field_name='team_name',lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ['team_name']
