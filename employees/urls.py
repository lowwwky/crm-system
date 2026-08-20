from django.urls import path

from employees.views import employee_list

app_name = 'employees'

urlpatterns = [
    path('show-employee/', employee_list, name='list'),
]