from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Technology_option', Technology_optionViewSet,basename='Technology_option')
router.register('Technology', TechnologyViewSet,basename='Technology')
router.register('Payment_method', Payment_methodViewSet,basename='Payment_method')
router.register('Tax', TaxViewSet,basename='Tax')


urlpatterns = [
    path('',include(router.urls))
] 
