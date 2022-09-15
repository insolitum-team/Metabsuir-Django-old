from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField


class Section(models.Model):
    name = models.CharField('Название секции', max_length=255)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField('Название темы', max_length=255)
    date = models.DateTimeField('Дата создания')
    main_post = RichTextField()
    author = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, blank=False, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.TextField('Содержание')
    theme = models.ForeignKey(Theme, blank=False, null=False, on_delete=models.CASCADE)
    reply_to = models.IntegerField('Ответ на')
    sender = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата отправки')
