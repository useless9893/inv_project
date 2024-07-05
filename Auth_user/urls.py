from django.urls import path ,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('city', CityViewSet,basename='City')
router.register('state', StateViewSet,basename='State')
router.register('country', CountryViewSet,basename='Country')

urlpatterns = [
     path('',include(router.urls)),
     path('login/', LoginView.as_view()),
     path('user/', get_coreuser),
]
