from django.db import models
from candidates.models import HireCard
from employees.models import EmployeeCard

class HRCalendar(models.Model):
    EVENT_TYPES = [
        ('interview','собеседование'),
        ('company_meeting', 'корпоративная встреча'),
        ('company_event', 'корпоративное мероприятие'),
        ('employee_birthday', 'день рождения сотрудника'),
    ]
    event_type = models.CharField(choices=EVENT_TYPES, max_length=50, default='company_meeting',verbose_name='Тип события')
    title = models.CharField(max_length=250, blank=True, verbose_name='Название')
    start_date = models.DateTimeField(null=True,verbose_name='Начало встречи')
    end_date = models.DateTimeField(null=True,verbose_name='Конец встречи')
    description = models.TextField(null=True,verbose_name='Описание')

    candidate = models.ForeignKey(
        HireCard,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Претендент на должность'
    )

    employee = models.ForeignKey(
        EmployeeCard,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Сотрудник компании'
    )

    class Meta:
        verbose_name = 'Событие HR'
        verbose_name_plural = 'События HR'

    def __str__(self):
        return f'{self.event_type} | {self.title} | {self.start_date} | {self.end_date} | {self.description}'
