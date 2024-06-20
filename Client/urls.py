from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Technology_option', Technology_optionViewSet,basename='Technology_option')
router.register('Technology', TechnologyViewSet,basename='Technology')
router.register('Payment_method', Payment_methodViewSet,basename='Payment_method')
router.register('Tax', TaxViewSet,basename='Tax')



urlpatterns = [
    path('',include(router.urls)),
    path('client/',ClientAPI.as_view()),
    path('invoice/',InvoiceAPI.as_view()),
    path('team/',TeamAPIView.as_view()),
    path('project/',ProjectAPIView.as_view()),
<<<<<<< HEAD
    path('invoice_item/',InvoiceitemAPI.as_view())
=======
    path('payment/',PaymentAPIView.as_view()),
    
>>>>>>> 8435e3f9de2e7703a2c7d1381689d181e9e62e6e
] 
