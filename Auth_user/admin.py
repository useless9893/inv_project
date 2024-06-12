from django.contrib import admin
from .models import *
from .models 

class CoreUserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','contact')
    list_editable = ('email','contact')

admin.site.register(CoreUser,CoreUserAdmin)