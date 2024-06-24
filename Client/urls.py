from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('Technology_option', Technology_optionViewSet,basename='Technology_option')
router.register('Technology', TechnologyViewSet,basename='Technology')
router.register('Payment_method', Payment_methodViewSet,basename='Payment_method')
router.register('Tax', TaxViewSet,basename='Tax')



urlpatterns = [
    path('api',include(router.urls)),
    path('client/',ClientAPI.as_view()),
    path('client_filter/', ClientListView.as_view()),
    path('invoice/',InvoiceAPI.as_view()),
    path('invoice_filter/<int:id>/',invoicefilter),
    path('team/',TeamAPIView.as_view()),
    path('project/',ProjectAPIView.as_view()),
    path('project_filter/',projectFilter),
    path('invoice_item/',InvoiceitemAPI.as_view()),
    path('payment/',PaymentAPIView.as_view()),
    path('technology_filter/',TechnologyListView.as_view()),
    path('team_filter/',TeamListView.as_view())
    
] 



