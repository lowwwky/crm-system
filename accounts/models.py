from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='person_photos', null=True, blank = True, verbose_name='Фотография')
    notes = models.TextField(verbose_name="Заметки", blank=True)
    birthdate = models.DateTimeField(verbose_name='Дата рождения',blank=True, null=True)

