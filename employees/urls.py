from django.urls import path

from employees.views import employee_list,employee_info

app_name = 'employees'

urlpatterns = [
    path('show-employee/', employee_list, name='employees'),
    path('employee-info/', employee_info, name='employee-info'),
]