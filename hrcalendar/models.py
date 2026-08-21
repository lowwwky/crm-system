from django.db import models

class HRCalendar(models.Model):
    class EventStatus(models.TextChoices):
        INTERVIEW = 'interview','собеседование'
        COMPANY_MEETING = 'company_meeting', 'корпоративная встреча'
        COMPANY_EVENT = 'company_event', 'корпоративное мероприятие'
        EMPLOYEE_BIRTHDAY = 'employee_birthday', 'день рождения сотрудника'

    event_type = models.CharField(choices=EventStatus.choices, max_length=50, default=EventStatus.COMPANY_MEETING,verbose_name='Тип события')
    title = models.CharField(max_length=250, blank=True, verbose_name='Название')
    start_date = models.DateTimeField(null=True,verbose_name='Начало встречи')
    end_date = models.DateTimeField(null=True,verbose_name='Конец встречи')
    description = models.TextField(blank=True,verbose_name='Описание', null=True)

    candidate = models.ForeignKey(
        'candidates.HireCard',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Претендент на должность',
        related_name='candidate',
    )

    employee = models.ForeignKey(
        'employees.EmployeeCard',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Сотрудник компании',
        related_name='employee',
    )

    class Meta:
        verbose_name = 'Событие HR'
        verbose_name_plural = 'События HR'

    def __str__(self):
        return f'{self.event_type} | {self.title} | {self.start_date} | {self.end_date} | {self.description}'
