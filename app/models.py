from django.contrib.auth.models import User
from django.db import models


class Section(models.Model):
    name = models.CharField('Название секции', max_length=255)

class Theme(models.Model):
    name = models.CharField('Название темы', max_length=255)
    date = models.DateTimeField('Дата создания')
    main_post = models.TextField('Главный пост')
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE)

class Message(models.Model):
    content = models.TextField('Содержание')
    theme = models.ForeignKey(Theme, blank=False, null=False, on_delete=models.CASCADE)
    reply_to = models.IntegerField('Ответ на')
    sender = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата отправки')

