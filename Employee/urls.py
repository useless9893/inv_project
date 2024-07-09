from django.urls import path,include
from .views import *



urlpatterns = [
    path('employee/',EmployeeAPI.as_view()),
    path('employee_filter/',EmployeeListView.as_view())

 

]

