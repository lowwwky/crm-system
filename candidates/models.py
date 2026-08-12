from django.db import models
from CRMSystem.models import PersonCard

# Create your models here.

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