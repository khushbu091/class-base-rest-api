from django.urls import path
from .views import *
urlpatterns=[
    path('', EmployeeList.as_view()),
]