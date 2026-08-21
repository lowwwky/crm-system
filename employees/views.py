from django.shortcuts import render, get_object_or_404

from employees.models import EmployeeCard

def employee_list(request):
    employees = EmployeeCard.objects.all()
    context = {
        'title':'Сотрудники',
        'employees': employees,
        'employees_amount': employees.count(),
    }
    return render(request, 'employees/employee-list.html', context=context)

def employee_info(request, employee_id):
    employee = get_object_or_404(EmployeeCard, pk=employee_id)
    context = {
        'title': 'Сотрудник',
        'employee': employee,
    }
    return render(request,'employees/employee-info.html', context=context)

def employee_add(request):
    ...


def employee_edit(request):
    ...

def employee_delete(request, employee_id):
    ...

def employee_filter(request):
    ...