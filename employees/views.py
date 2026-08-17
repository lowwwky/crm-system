from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
    return render(request, 'employees/employee-list.html', {'employees': []})