from django.contrib import admin

# Register your models here.

from .models import Technology_option
from .models import Technology
from .models import Payment_method
from .models import Tax



@admin.register(Technology_option)
class Technology_optionAdmin(admin.ModelAdmin):
    list_display = Technology_option.DisplayField


@admin.register(Technology)
class TechnolongyAdmin(admin.ModelAdmin):
    list_display = Technology.DisplayField


@admin.register(Payment_method)
class Payment_mthodAdmin(admin.ModelAdmin):
    list_display = Payment_method.DisplayField


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = Tax.DisplayField