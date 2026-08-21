from django import forms

from .models import EmployeeCard

class CreateEmployee(forms.ModelForm):

    class Meta:
        model = EmployeeCard
        fields = ['salary','department','start_date','position']

class EditEmployee(forms.ModelForm):

    class Meta:
        model = EmployeeCard
        fields = ['salary', 'department']
