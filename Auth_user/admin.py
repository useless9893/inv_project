from django.contrib import admin
from .models import *

@admin.register(CoreUser)
class CoreUserAdmin(admin.ModelAdmin):
    list_display = CoreUser.DisplayField
    list_editable = ('email','contact')
 

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = Role.DisplayField


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = State.DisplayField


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = City.DisplayField

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = Country.DisplayField