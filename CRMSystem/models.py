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





