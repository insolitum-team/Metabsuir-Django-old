from django.contrib.auth.models import User
from django.db import models


class UserOptional(models.Model):
    faculty = models.CharField('Факультет', max_length=5)
    specialty = models.CharField('Специальность', max_length=255)
    group = models.CharField('Номер группы', max_length=6)
    description = models.TextField('Описание', max_length=1000)
    tg_link = models.URLField('Ссылка на телеграм')
    user = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
