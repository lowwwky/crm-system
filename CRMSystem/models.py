from django.db import models

class PersonCard(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=200, null=True, verbose_name='Отчество')
    birthdate = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    image = models.ImageField(upload_to='person_photos', null=True, blank = True, verbose_name='Фотография')
    notes = models.TextField(null=True, blank=True, verbose_name='Заметки')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    archived_at = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.surname} {self.name}'


class EmployeeCard(PersonCard):
    employee_position = models.CharField(max_length=200, verbose_name='Позиция')
    employee_department = models.CharField(max_length=200, verbose_name='Отдел')
    employee_start_date = models.DateField(null=False,  verbose_name='Дата начала работы')
    salary = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Заработная плата')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.surname} {self.name} | {self.employee_position}/{self.employee_department}'


class HireCard(PersonCard):
    HIRE_STATUS = [
        ('contact', 'связались'),
        ('interview', 'собеседование'),
        ('offer','приглашение на работу'),
        ('decline','отказ'),
    ]
    desired_position = models.CharField(max_length=250, verbose_name='Желаемая позиция')
    resume_link = models.URLField(null=False, blank = False, verbose_name='Резюме')
    interview_date = models.DateTimeField(null=True, blank=True, verbose_name='Время собеседования')
    status = models.CharField(max_length=50, choices=HIRE_STATUS, default='contact', verbose_name='Статус')


    class Meta:
        verbose_name = 'Соискатель'
        verbose_name_plural = 'Соискатели'

    def __str__(self):
        return f'{self.surname} {self.name} | {self.desired_position} | {self.resume_link}'

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
    )

    employee = models.ForeignKey(
        EmployeeCard,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Событие HR'
        verbose_name_plural = 'События HR'

    def __str__(self):
        return f'{self.event_type} | {self.title} | {self.start_date} | {self.end_date} | {self.description}'





