from django.db import models
from CRMSystem.models import PersonCard

class EmployeeCard(PersonCard):
    position = models.CharField(max_length=200, verbose_name='Позиция')
    department = models.CharField(max_length=200, verbose_name='Отдел')
    start_date = models.DateField(null=False,  verbose_name='Дата начала работы')
    salary = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Заработная плата')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.surname} {self.name} | {self.position}/{self.department}'