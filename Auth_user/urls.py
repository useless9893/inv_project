from django.urls import path ,include
from .views import *

urlpatterns = [
     path('login/', LoginView.as_view()),
     path('user/', get_coreuser),
]
